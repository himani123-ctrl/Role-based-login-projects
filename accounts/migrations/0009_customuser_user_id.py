# Generated by Django 5.0.7 on 2024-09-30 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_customuser_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(blank=True, max_length=30, null=True, unique=True),
        ),
    ]
