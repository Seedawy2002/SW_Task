from django.contrib import admin
from .models import ProcessedData, KPIInfo, KPIAssetLink

admin.site.register(ProcessedData)
admin.site.register(KPIInfo)
admin.site.register(KPIAssetLink)
