# Generated by Django 5.1.6 on 2025-03-04 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_categories_options_alter_categories_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='quamtity',
        ),
    ]
