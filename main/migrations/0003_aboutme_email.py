# Generated by Django 4.2.2 on 2023-06-23 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_hobby_icon_remove_mycharacter_icon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutme',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
