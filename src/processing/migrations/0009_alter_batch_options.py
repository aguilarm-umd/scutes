# Generated by Django 4.2.3 on 2024-05-27 17:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0008_alter_batch_assigned_to'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='batch',
            options={'verbose_name_plural': 'Batches'},
        ),
    ]