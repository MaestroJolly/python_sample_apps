# Generated by Django 2.1.4 on 2019-01-16 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=30)),
                ('customer_email', models.CharField(max_length=30)),
                ('status', models.CharField(max_length=10)),
                ('amount', models.IntegerField()),
                ('currency', models.CharField(max_length=3)),
                ('transaction_ref', models.CharField(max_length=35)),
                ('flw_ref', models.CharField(max_length=35)),
                ('date_created', models.DateField()),
            ],
        ),
    ]
