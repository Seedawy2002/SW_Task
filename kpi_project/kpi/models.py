from django.db import models

class ProcessedData(models.Model):
    asset_id = models.CharField(max_length=50)
    attribute_id = models.CharField(max_length=50)
    timestamp = models.CharField(max_length=50)  # Store timestamp as string, including [UTC]
    value = models.CharField(max_length=50)      # Store value as string
    
    def __str__(self):
        return f"{self.asset_id} - {self.attribute_id} - {self.timestamp} - {self.value}"

class KPIInfo(models.Model):
    name = models.CharField(max_length=100)
    expression = models.CharField(max_length=255)  # Store the expression as a string
    description = models.TextField(blank=True, null=True)  # Optional description field

    def __str__(self):
        return f"{self.name} - {self.expression}"

# models.py

class KPIAssetLink(models.Model):
    asset_id = models.CharField(max_length=50)
    attribute_id = models.CharField(max_length=50, default="default_attribute")  # Add a default here
    kpi = models.ForeignKey(KPIInfo, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('asset_id', 'attribute_id')

    def __str__(self):
        return f"KPI Link for Asset {self.asset_id} and Attribute {self.attribute_id} - KPI: {self.kpi.name}"
