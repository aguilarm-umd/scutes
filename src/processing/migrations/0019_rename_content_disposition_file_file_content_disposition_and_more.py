# Generated by Django 4.2.3 on 2023-12-01 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('processing', '0018_remove_file_title_file_content_disposition_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='content_disposition',
            new_name='file_content_disposition',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='content_id',
            new_name='file_content_id',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='content_type',
            new_name='file_content_type',
        ),
        migrations.RenameField(
            model_name='file',
            old_name='name',
            new_name='file_name',
        ),
    ]