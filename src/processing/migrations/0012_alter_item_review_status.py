# Generated by Django 4.2.3 on 2023-09-29 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0011_alter_batch_assigned_to_alter_item_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='review_status',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
