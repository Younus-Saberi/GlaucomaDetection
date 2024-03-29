# Generated by Django 3.2.12 on 2024-03-27 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelapi', '0002_auto_20240323_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProcessedImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disc_area', models.FloatField(max_length=50)),
                ('cup_area', models.FloatField(max_length=50)),
                ('cupdisc_ratio', models.FloatField(max_length=50)),
                ('s3_link', models.URLField()),
                ('uploaded_image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelapi.uploadedimage')),
            ],
        ),
    ]