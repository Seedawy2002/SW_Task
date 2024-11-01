# kpi/apps.py
import time
import os
import json
import re
from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError
from django.db import connection
from django.conf import settings


class KPIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kpi'

    def ready(self):
        # Delay the CSV processing until migrations are applied and database is ready
        if settings.DEBUG:  # Only run auto-processing in DEBUG mode to avoid unwanted startup behavior
            self.auto_process_csv_on_startup()

    def auto_process_csv_on_startup(self):
        # Check if the database is available and migrations are applied
        try:
            # Check if the tables exist by executing a lightweight query
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='kpi_processeddata';")
                if not cursor.fetchone():
                    print("Database tables are not yet ready. Skipping CSV processing.")
                    return
        except (OperationalError, ProgrammingError):
            print("Database not available or migrations not applied. Skipping CSV processing.")
            return

        from .models import ProcessedData, KPIInfo, KPIAssetLink  # Import here to avoid early app registry access
        from .interpreter.interpreter import Interpreter  # Ensure interpreter path is correct

        print("Auto-processing CSV on startup...")
        file_path = os.path.join('data', 'data_source.csv')

        if not os.path.exists(file_path):
            print("File not found:", file_path)
            return

        with open(file_path, 'r') as f:
            for line in f:
                time.sleep(5)
                line = line.strip()
                if line:
                    try:
                        json_data = json.loads(line)
                        asset_id = json_data.get('asset_id')
                        if not asset_id or 'value' not in json_data or 'attribute_id' not in json_data:
                            print(f"Missing keys in line: {json_data}")
                            continue

                        value = json_data['value']
                        
                        # Check if value is numeric for standard processing
                        try:
                            numeric_value = float(value)
                        except ValueError:
                            numeric_value = None  # Set to None if not a number

                        kpi_link = KPIAssetLink.objects.filter(asset_id=asset_id).first()
                        if not kpi_link:
                            print(f"No KPI linked for asset_id {asset_id}")
                            continue

                        kpi = kpi_link.kpi
                        equation = kpi.expression
                        print("Evaluating Equation:", equation)
                        
                        # Check if the expression contains a Regex pattern
                        if equation.startswith("Regex("):
                            # Updated regex extraction to handle formats like Regex(value, '^dog')
                            match = re.search(r'Regex\(\s*value\s*,\s*["\'](.*?)["\']\s*\)', equation)
                            if match:
                                pattern = match.group(1)  # Extract the pattern
                                print("Using Regex Pattern:", pattern)
                                result = bool(re.match(pattern, str(value)))  # Ensure value is a string for regex matching
                                print("Regex Match Result:", result)
                            else:
                                print(f"Invalid Regex format for KPI ID {kpi.id}. Skipping.")
                                continue  # Skip this line if regex is not well-formed
                        else:
                            # Standard expression processing using the Interpreter
                            if numeric_value is None:
                                print(f"Non-numeric value '{value}' found for non-regex KPI ID {kpi.id}. Skipping.")
                                continue
                            context = {"value": numeric_value}
                            interpreter = Interpreter(equation)
                            result = interpreter.interpret(context)

                        # Prepare data for saving
                        json_data['value'] = str(result)
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
                        print("Saved processed entry:", processed_entry)

                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON in line: {line}, error: {e}")
                    except ValueError as e:
                        print(f"Error processing value in line: {line}, error: {e}")
                    except OperationalError:
                        print("Database error: Ensure that migrations are applied.")
                    except Exception as e:
                        print(f"Unexpected error: {e}")

        print("Auto-processing CSV complete.")
