# Generated by Django 3.2.9 on 2022-02-09 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesinvoicedetails',
            name='ProductId',
        ),
        migrations.AddField(
            model_name='salesinvoicedetails',
            name='ProductId',
            field=models.ManyToManyField(to='api.Product'),
        ),
        migrations.RemoveField(
            model_name='salesinvoicedetails',
            name='SalesInvoiceId',
        ),
        migrations.AddField(
            model_name='salesinvoicedetails',
            name='SalesInvoiceId',
            field=models.ManyToManyField(to='api.SalesInvoice'),
        ),
    ]
