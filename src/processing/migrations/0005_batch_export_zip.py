# Generated by Django 4.2.3 on 2024-04-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("processing", "0004_batch_last_export"),
    ]

    operations = [
        migrations.AddField(
            model_name="batch",
            name="export_zip",
            field=models.FileField(null=True, upload_to="export"),
        ),
    ]
