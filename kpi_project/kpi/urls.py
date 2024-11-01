from django.urls import path
from .views import (
    KPIUploadView,
    ApplyKPIEquationView,
    KPIListCreateView,
    KPIAssetLinkView,
    ProcessedDataListView,
    KPIAssetLinkListView,
)


urlpatterns = [
    path('process-data/', KPIUploadView.as_view(), name='kpi-process-data'),
    path('apply-kpi/<str:asset_id>/<str:value>/', ApplyKPIEquationView.as_view(), name='apply-kpi'),
    path('kpi/', KPIListCreateView.as_view(), name='kpi-list-create'),
    path('link-asset/', KPIAssetLinkView.as_view(), name='link-asset'),
    path('processed-data/', ProcessedDataListView.as_view(), name='processed-data'),
    path('asset-kpi-links/', KPIAssetLinkListView.as_view(), name='asset-kpi-links'),
]
