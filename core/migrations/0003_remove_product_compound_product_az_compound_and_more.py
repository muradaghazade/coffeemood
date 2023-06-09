# Generated by Django 4.1.7 on 2023-03-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_image_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='compound',
        ),
        migrations.AddField(
            model_name='product',
            name='az_compound',
            field=models.TextField(default='', verbose_name='AZ Compound'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='en_compound',
            field=models.TextField(default='', verbose_name='EN Compound'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='ru_compound',
            field=models.TextField(default='', verbose_name='RU Compound'),
            preserve_default=False,
        ),
    ]
