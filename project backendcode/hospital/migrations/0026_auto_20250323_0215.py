# Generated by Django 3.0.5 on 2025-03-22 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0025_uploadedfile'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='gender',
            field=models.CharField(default='Male', max_length=6),
        ),
        migrations.AddField(
            model_name='patient',
            name='neighbourhood',
            field=models.CharField(default='1', max_length=10),
        ),
    ]
