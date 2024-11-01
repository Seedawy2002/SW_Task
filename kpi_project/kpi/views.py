import json
import os
import time
from django.http import JsonResponse
from django.views import View
from .models import ProcessedData, KPIInfo, KPIAssetLink
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .interpreter.interpreter import Interpreter  # Ensure this path is correct
from django.http import HttpResponse
import re


def home_view(request):
    # Redirect to Swagger documentation by default
    #return redirect('/swagger/')
    # Alternatively, you can return a simple message
    return HttpResponse("<h1>Welcome to the KPI API</h1><p>Visit <a href='/swagger/'>Swagger Documentation</a> for API details.</p>")

@extend_schema(exclude=True)
class KPIUploadView(APIView):
    def get(self, request):
        file_path = os.path.join('data', 'data_source.csv')
        processed_data = []

        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    try:
                        json_data = json.loads(line)
                        if 'value' in json_data:
                            numeric_value = float(json_data['value'])
                            processed_value = self.apply_equation(numeric_value)
                            json_data['value'] = str(processed_value)

                        original_attribute_id = json_data['attribute_id']
                        json_data['attribute_id'] = f"output_{original_attribute_id}"
                        json_data['timestamp'] = f"{json_data['timestamp']}[UTC]"

                        processed_entry = ProcessedData(
                            asset_id=json_data['asset_id'],
                            attribute_id=json_data['attribute_id'],
                            timestamp=json_data['timestamp'],
                            value=json_data['value']
                        )
                        processed_entry.save()
                        processed_data.append(json_data)
                        time.sleep(5)
                    
                    except (json.JSONDecodeError, ValueError) as e:
                        print(f"Error processing line: {line}, error: {e}")
        
        return JsonResponse({'processed_data': processed_data})

    def apply_equation(self, value):
        return value * 2 + 3

@extend_schema(exclude=True)
class ApplyKPIEquationView(APIView):
    def get(self, request, kpi_id, value):
        try:
            # Retrieve the KPI and its expression
            kpi = KPIInfo.objects.get(id=kpi_id)
            expression = kpi.expression
            print("Received Expression:", expression)

            # Check if expression is of the form "Regex(value, pattern)"
            if expression.startswith("Regex("):
                # Use regex to extract the pattern from the expression
                match = re.search(r'Regex\(\s*value\s*,\s*"(.*?)"\s*\)', expression)
                if match:
                    pattern = match.group(1)  # Extract the pattern inside quotes
                    print("Using Regex Pattern:", pattern)
                    result = bool(re.match(pattern, value))
                else:
                    return JsonResponse({"error": "Invalid Regex expression format"}, status=400)
            
            else:
                # For non-regex expressions, try converting the value to a float
                try:
                    numeric_value = float(value)
                    context = {"value": numeric_value}
                    interpreter = Interpreter(expression)
                    result = interpreter.interpret(context)
                except ValueError:
                    # If conversion fails, it's likely due to a non-numeric value provided for numeric expressions
                    return JsonResponse({"error": "Non-numeric value provided for a numeric expression."}, status=400)

            # Return the final result in the JSON response
            return JsonResponse({"kpi_id": kpi_id, "value": value, "result": result})

        except KPIInfo.DoesNotExist:
            # Handle the case when KPI is not found
            return JsonResponse({"error": "KPI not found"}, status=404)
        except Exception as e:
            # Handle any other unexpected errors
            return JsonResponse({"error": str(e)}, status=500)


@method_decorator(csrf_exempt, name='dispatch')
@extend_schema(tags=["SW_Task_API"])
@extend_schema_view(
    get=extend_schema(
        summary="List all KPIs",
        description="Returns a list of all available KPIs.",
        responses={200: JsonResponse}
    ),
    post=extend_schema(
        summary="Create a new KPI",
        description="Creates a new KPI with a given name, expression, and description.",
        request={
            "application/json": {
                "name": "New KPI Name",
                "expression": "KPI expression",
                "description": "Description of the KPI"
            }
        },
        responses={201: JsonResponse}
    )
)
class KPIListCreateView(APIView):
    def get(self, request):
        kpis = KPIInfo.objects.all()
        kpi_data = [{"id": kpi.id, "name": kpi.name, "expression": kpi.expression, "description": kpi.description} for kpi in kpis]
        return JsonResponse({"kpis": kpi_data})

    def post(self, request):
        data = json.loads(request.body)
        name = data.get("name")
        expression = data.get("expression")
        description = data.get("description", "")

        new_kpi = KPIInfo(name=name, expression=expression, description=description)
        new_kpi.save()

        return JsonResponse({
            "id": new_kpi.id,
            "name": new_kpi.name,
            "expression": new_kpi.expression,
            "description": new_kpi.description
        }, status=201)


@method_decorator(csrf_exempt, name='dispatch')
@extend_schema(tags=["SW_Task_API"])
@extend_schema_view(
    post=extend_schema(
        summary="Link Asset to KPI",
        description="Creates a link between an asset and a KPI.",
        request={
            "application/json": {
                "asset_id": "Asset ID to link",
                "kpi_id": "ID of the KPI"
            }
        },
        responses={201: JsonResponse}
    )
)
class KPIAssetLinkView(APIView):
    def post(self, request):
        data = json.loads(request.body)
        asset_id = data.get("asset_id")
        kpi_id = data.get("kpi_id")

        try:
            kpi = KPIInfo.objects.get(id=kpi_id)
            link = KPIAssetLink(kpi=kpi, asset_id=asset_id)
            link.save()
            return JsonResponse({"id": link.id, "kpi_id": link.kpi.id, "asset_id": link.asset_id}, status=201)
        
        except KPIInfo.DoesNotExist:
            return JsonResponse({"error": "KPI not found"}, status=404)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

@extend_schema(tags=["SW_Task_API"])
@extend_schema_view(
    get=extend_schema(
        summary="List all asset-KPI links",
        description="Returns a list of all links between assets and KPIs.",
        responses={200: JsonResponse}
    )
)
class KPIAssetLinkListView(APIView):
    def get(self, request):
        links = KPIAssetLink.objects.all()
        data = [{"id": link.id, "asset_id": link.asset_id, "kpi_id": link.kpi.id, "kpi_name": link.kpi.name} for link in links]
        return JsonResponse({"asset_kpi_links": data})

@extend_schema(tags=["SW_Task_API"])
@extend_schema_view(
    get=extend_schema(
        summary="List all processed data",
        description="Returns a list of all processed data entries.",
        responses={200: JsonResponse}
    )
)
class ProcessedDataListView(APIView):
    def get(self, request):
        processed_data = ProcessedData.objects.all()
        data = [{"asset_id": entry.asset_id, "attribute_id": entry.attribute_id, "timestamp": entry.timestamp, "value": entry.value} for entry in processed_data]
        return JsonResponse({"processed_data": data})