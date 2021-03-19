# Generated by Django 2.2 on 2020-03-20 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coronaapi', '0006_hackathon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Total',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalConfirmed', models.IntegerField(blank=True, null=True, verbose_name='Total confirm cases in country')),
                ('totalDeaths', models.IntegerField(blank=True, null=True, verbose_name='Total death cases in country')),
                ('totalRecovered', models.IntegerField(blank=True, null=True, verbose_name='Total recovered cases in country')),
            ],
        ),
        migrations.DeleteModel(
            name='Cities',
        ),
    ]