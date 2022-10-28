# Generated by Django 4.1.2 on 2022-10-28 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalInterestKeyWord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_keyword', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='RegionInterests',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalInterest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField()),
                ('trends', models.IntegerField()),
                ('is_partial', models.BooleanField()),
                ('search_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='search_key', to='google_trends.historicalinterestkeyword')),
            ],
        ),
    ]
