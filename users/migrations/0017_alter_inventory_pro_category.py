# Generated by Django 4.0.1 on 2022-02-05 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_inventory_pro_sold_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='pro_category',
            field=models.CharField(choices=[('Filing Supplies', 'Filing Supplies'), ('Paper Supplies', 'Paper Supplies'), ('School and Office Essentials', 'School and Office Essentials'), ('Writing Supplies', 'Writing Supplies'), ('Books', 'Books'), ('Unassigned', 'Unassigned')], default='Unassigned', max_length=100, verbose_name='Category'),
        ),
    ]
