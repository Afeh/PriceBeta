# Generated by Django 3.2.14 on 2022-07-24 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('priceBetaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image_url',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='purchase_link',
            field=models.CharField(max_length=250, null=True),
        ),
    ]