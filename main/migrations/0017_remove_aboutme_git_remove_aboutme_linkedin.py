# Generated by Django 4.2.2 on 2023-06-26 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_rename_google_social_link_social_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutme',
            name='git',
        ),
        migrations.RemoveField(
            model_name='aboutme',
            name='linkedin',
        ),
    ]
