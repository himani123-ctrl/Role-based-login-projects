# Generated by Django 5.0.7 on 2024-09-30 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_remove_customuser_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_id',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
    ]
