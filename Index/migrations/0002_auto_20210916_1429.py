# Generated by Django 3.2.6 on 2021-09-16 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='approach',
            name='css_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='service',
            name='css_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='strategy',
            name='css_name',
            field=models.CharField(max_length=30),
        ),
    ]
