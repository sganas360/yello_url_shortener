# Generated by Django 4.0.4 on 2022-05-09 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='encoded_url',
            field=models.URLField(blank=True, null=True, unique=True),
        ),
    ]
