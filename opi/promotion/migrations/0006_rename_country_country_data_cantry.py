# Generated by Django 3.2.6 on 2023-03-18 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promotion', '0005_auto_20230318_1720'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country_data',
            old_name='country',
            new_name='cantry',
        ),
    ]