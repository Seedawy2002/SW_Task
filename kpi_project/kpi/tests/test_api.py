from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from kpi.models import KPIInfo, KPIAssetLink

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_kpis(self):
        url = reverse('kpi-list-create')  # Updated URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_kpi(self):
        url = reverse('kpi-list-create')  # Ensure 'kpi-list-create' is the correct name in urls.py
        data = {
            "name": "Test KPI",
            "expression": "value * 2",
            "description": "A test KPI"
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Use response.json() to retrieve the data
        response_data = response.json()
        self.assertEqual(response_data['name'], "Test KPI")


    def test_link_asset_to_kpi(self):
        # Create a KPI first to link
        kpi = KPIInfo.objects.create(name="Link Test KPI", expression="value * 3")
        url = reverse('link-asset')  # Updated URL name
        data = {
            "asset_id": "123",
            "kpi_id": kpi.id
        }
        response = self.client.post(url, data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_kpi_asset_links(self):
        url = reverse('asset-kpi-links')  # Updated URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_processed_data(self):
        url = reverse('processed-data')  # Updated URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
