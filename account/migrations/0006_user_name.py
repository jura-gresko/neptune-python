# Generated by Django 2.0.4 on 2018-05-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180517_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=255, null=True, verbose_name='name'),
        ),
    ]