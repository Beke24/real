# Generated by Django 5.1.6 on 2025-02-21 16:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atendance',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
