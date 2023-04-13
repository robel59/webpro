# Generated by Django 3.2.6 on 2023-03-03 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webuser', '0018_alter_service_payment_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='domainname_cost',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=15, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('rday', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]