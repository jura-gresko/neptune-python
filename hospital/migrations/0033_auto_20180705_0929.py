# Generated by Django 2.0.4 on 2018-07-05 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0032_item_cost_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='system_cost',
        ),
        migrations.RemoveField(
            model_name='item',
            name='unit_cost',
        ),
        migrations.AddField(
            model_name='item',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=20),
        ),
    ]