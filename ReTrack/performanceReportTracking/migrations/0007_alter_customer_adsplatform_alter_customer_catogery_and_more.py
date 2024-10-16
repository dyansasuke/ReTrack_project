# Generated by Django 4.2.4 on 2024-09-02 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('performanceReportTracking', '0006_customerpackage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='adsPlatform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performanceReportTracking.customerplatform'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='catogery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performanceReportTracking.customercatogery'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performanceReportTracking.customerpackage'),
        ),
    ]
