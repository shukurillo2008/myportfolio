# Generated by Django 4.2.2 on 2023-06-24 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_aboutme_degree'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='git',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='aboutme',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]