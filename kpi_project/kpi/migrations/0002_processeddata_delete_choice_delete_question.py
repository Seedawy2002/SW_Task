# Generated by Django 5.1.2 on 2024-10-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kpi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_id', models.CharField(max_length=50)),
                ('attribute_id', models.CharField(max_length=50)),
                ('timestamp', models.CharField(max_length=50)),
                ('value', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
