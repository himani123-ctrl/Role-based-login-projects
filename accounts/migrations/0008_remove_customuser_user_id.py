# Generated by Django 5.0.7 on 2024-09-30 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_expensereport_user_customuser_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='user_id',
        ),
    ]
