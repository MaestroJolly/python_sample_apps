# Generated by Django 2.1.4 on 2019-01-16 15:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webhook', '0003_auto_20190116_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='transaction_type',
            field=models.CharField(default=django.utils.timezone.now, max_length=20),
            preserve_default=False,
        ),
    ]
