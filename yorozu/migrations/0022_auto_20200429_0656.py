# Generated by Django 2.2.2 on 2020-04-29 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yorozu', '0021_auto_20200429_0615'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='plan_list',
        ),
        migrations.AddField(
            model_name='profile',
            name='plan_list',
            field=models.ManyToManyField(default='', null=True, to='yorozu.Plan', verbose_name='プランリスト'),
        ),
    ]
