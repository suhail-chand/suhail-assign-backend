# Generated by Django 4.0.6 on 2022-07-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default='Apple', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
