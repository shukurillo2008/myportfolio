# Generated by Django 4.2.2 on 2023-06-24 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_social'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='texnology',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
