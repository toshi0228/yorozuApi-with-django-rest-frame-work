# Generated by Django 2.2.2 on 2020-04-04 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yorozu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='名称')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='プランタイトル')),
                ('description', models.CharField(max_length=255, verbose_name='プランの説明')),
                ('image', models.ImageField(default='', upload_to='', verbose_name='イメージ画像')),
                ('price', models.PositiveIntegerField(default=0, verbose_name='料金')),
                ('tags', models.ManyToManyField(to='yorozu.Tag')),
            ],
            options={
                'verbose_name_plural': 'プラン',
            },
        ),
    ]
