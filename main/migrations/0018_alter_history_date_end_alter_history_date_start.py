# Generated by Django 4.2.2 on 2023-06-26 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_remove_aboutme_git_remove_aboutme_linkedin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='date_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='history',
            name='date_start',
            field=models.DateField(blank=True, null=True),
        ),
    ]
