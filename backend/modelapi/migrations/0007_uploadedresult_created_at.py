# Generated by Django 3.2.12 on 2024-05-08 04:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('modelapi', '0006_auto_20240424_2317'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedresult',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
