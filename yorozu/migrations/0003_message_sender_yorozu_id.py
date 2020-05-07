# Generated by Django 2.2.2 on 2020-05-09 14:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yorozu', '0002_auto_20200509_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='sender_yorozu_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='yorozu.Profile', verbose_name='送信者'),
        ),
    ]
