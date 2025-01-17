# Generated by Django 3.2.8 on 2021-11-07 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KkdayTainan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('rating_count', models.IntegerField()),
                ('star', models.FloatField()),
                ('order_count', models.IntegerField()),
                ('market_price', models.IntegerField()),
                ('selling_price', models.IntegerField()),
                ('img_url', models.CharField(max_length=255)),
                ('data_url', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'kkday_tainan',
                'managed': False,
            },
        ),
    ]
