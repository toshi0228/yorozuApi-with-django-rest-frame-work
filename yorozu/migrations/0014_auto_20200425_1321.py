# Generated by Django 2.2.2 on 2020-04-25 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yorozu', '0013_auto_20200425_1319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='pan_list',
            new_name='plan_list',
        ),
        migrations.AlterField(
            model_name='plan',
            name='yorozuya_profile',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='yorozu.Profile'),
        ),
    ]
