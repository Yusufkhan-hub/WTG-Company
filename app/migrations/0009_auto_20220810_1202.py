# Generated by Django 3.2.1 on 2022-08-10 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_product_product_s'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_s',
            name='finish',
            field=models.CharField(default='', max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product_s',
            name='standard_thinckness',
            field=models.CharField(max_length=150),
        ),
    ]
