# Generated by Django 3.2.6 on 2023-03-15 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0023_webservice_unique_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webservice',
            name='unique_field',
            field=models.CharField(default='a40b3f5f17bf476589f33b5f486ccef2', editable=False, max_length=32, unique=True),
        ),
    ]
