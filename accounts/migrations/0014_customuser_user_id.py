# Generated by Django 5.0.7 on 2024-09-30 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_remove_customuser_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_id',
            field=models.PositiveIntegerField(null=True, unique=True),
        ),
    ]