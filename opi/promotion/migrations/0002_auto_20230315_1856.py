# Generated by Django 3.2.6 on 2023-03-15 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0014_use_autofields_for_pk'),
        ('webuser', '0022_auto_20230311_1109'),
        ('promotion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='daily_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=1)),
                ('rday', models.DateField(auto_now_add=True)),
                ('webservice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webuser.webservice')),
            ],
        ),
        migrations.CreateModel(
            name='vister_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('time', models.DateTimeField(null=True)),
                ('rday', models.DateField(auto_now_add=True)),
                ('webservice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webuser.webservice')),
            ],
        ),
        migrations.DeleteModel(
            name='MyEvent',
        ),
    ]
