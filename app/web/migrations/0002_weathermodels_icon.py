# Generated by Django 3.2.7 on 2021-10-24 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='weathermodels',
            name='icon',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
