# Generated by Django 2.1.2 on 2019-02-14 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brand', '0002_auto_20190214_0800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brandName',
            field=models.CharField(max_length=140),
        ),
    ]
