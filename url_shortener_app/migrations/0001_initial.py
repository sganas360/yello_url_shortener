# Generated by Django 4.0.4 on 2022-05-09 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField(max_length=2000, unique=True)),
                ('encoded_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
