# Generated by Django 4.0.1 on 2022-02-05 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_inventory_pro_sold_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='pro_sold',
            field=models.IntegerField(blank=True, null=True, verbose_name='Quantity Sold'),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='pro_totalsales',
            field=models.IntegerField(blank=True, null=True, verbose_name='Total Sale'),
        ),
    ]