# Generated by Django 2.0.4 on 2018-06-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('price', '0004_auto_20180615_0519'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='apply_type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Before doctor order'), (2, 'On doctor order'), (3, 'After doctor order')], default=2, verbose_name='Apply type'),
        ),
    ]
