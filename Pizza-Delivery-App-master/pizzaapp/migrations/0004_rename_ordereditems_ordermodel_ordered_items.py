# Generated by Django 3.2.6 on 2021-09-20 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizzaapp', '0003_ordermodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordermodel',
            old_name='ordereditems',
            new_name='ordered_items',
        ),
    ]
