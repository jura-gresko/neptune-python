# Generated by Django 2.0.4 on 2018-06-22 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('device', '0015_auto_20180622_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='category_feature',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='device.CategoryFeature'),
        ),
    ]