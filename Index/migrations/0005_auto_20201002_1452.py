# Generated by Django 3.1 on 2020-10-02 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0004_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='link',
            field=models.CharField(max_length=700),
        ),
    ]
