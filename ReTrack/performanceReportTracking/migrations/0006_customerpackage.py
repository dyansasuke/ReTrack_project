# Generated by Django 4.2.4 on 2024-09-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performanceReportTracking', '0005_customercatogery'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerPackage',
            fields=[
                ('pakej', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
