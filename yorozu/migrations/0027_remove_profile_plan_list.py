# Generated by Django 2.2.2 on 2020-04-30 12:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yorozu', '0026_auto_20200430_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='plan_list',
        ),
    ]
