# Generated by Django 5.0.7 on 2024-09-30 06:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_expensereport_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='packagereport',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='package_reports', to=settings.AUTH_USER_MODEL),
        ),
    ]
