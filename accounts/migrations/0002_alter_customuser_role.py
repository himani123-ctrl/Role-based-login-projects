# Generated by Django 5.1.1 on 2024-09-25 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('admin', 'Admin'), ('user', 'User'), ('enterprise', 'Enterprise')], default='user', max_length=20),
        ),
    ]
