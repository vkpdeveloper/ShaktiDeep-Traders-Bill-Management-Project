# Generated by Django 2.2.4 on 2019-11-25 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='bill_temp',
        ),
    ]
