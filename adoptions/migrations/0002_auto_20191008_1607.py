# Generated by Django 2.2.5 on 2019-10-08 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Pet',
        ),
        migrations.DeleteModel(
            name='Vaccine',
        ),
    ]
