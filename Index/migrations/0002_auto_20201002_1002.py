# Generated by Django 3.1 on 2020-10-02 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='descritin',
            new_name='description',
        ),
    ]
