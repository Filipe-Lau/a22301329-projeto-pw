# Generated by Django 4.0.6 on 2024-04-24 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='capa',
            field=models.ImageField(blank=True, upload_to='capas_albuns/'),
        ),
    ]