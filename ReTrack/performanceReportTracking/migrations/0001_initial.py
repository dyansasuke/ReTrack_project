# Generated by Django 4.2.4 on 2024-09-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staffID', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('staffName', models.TextField()),
                ('staffPassword', models.TextField()),
                ('staffEmail', models.TextField()),
            ],
        ),
    ]
