# Generated by Django 5.0.7 on 2024-09-26 08:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('your_name', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('report_from', models.CharField(max_length=100)),
                ('report_to', models.CharField(max_length=100)),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('invoice_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyFormData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('your_name', models.CharField(max_length=100)),
                ('company_gstin', models.CharField(max_length=50)),
                ('company_address', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('client_company', models.CharField(max_length=100)),
                ('client_gstin', models.CharField(max_length=50)),
                ('client_address', models.TextField()),
                ('client_city', models.CharField(max_length=100)),
                ('client_state', models.CharField(max_length=100)),
                ('client_country', models.CharField(max_length=100)),
                ('invoice', models.CharField(max_length=50)),
                ('datetime_field1', models.DateTimeField()),
                ('datetime_field2', models.DateTimeField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('notes', models.TextField(blank=True, null=True)),
                ('terms_conditions', models.TextField(blank=True, null=True)),
                ('invoice_id', models.CharField(blank=True, max_length=50, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('expense_description', models.CharField(max_length=255)),
                ('merchant', models.CharField(max_length=100)),
                ('amount', models.FloatField()),
                ('expense_report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='accounts.expensereport')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_desc', models.CharField(max_length=255)),
                ('qty', models.FloatField()),
                ('rate', models.FloatField()),
                ('gst_rate', models.PositiveIntegerField(choices=[(0, '0%'), (5, '5%'), (12, '12%'), (18, '18%'), (28, '28%')], default=0)),
                ('sgst', models.FloatField(default=0.0)),
                ('cgst', models.FloatField(default=0.0)),
                ('cess', models.FloatField(default=0.0)),
                ('myformdata', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='accounts.myformdata')),
            ],
        ),
    ]
