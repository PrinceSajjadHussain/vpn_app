# Generated by Django 4.2.13 on 2024-06-10 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vpn_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vpnuser',
            name='is_enabled',
            field=models.BooleanField(default=False),
        ),
    ]
