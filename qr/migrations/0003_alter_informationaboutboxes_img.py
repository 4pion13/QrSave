# Generated by Django 5.0.6 on 2024-05-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_informationaboutboxes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informationaboutboxes',
            name='img',
            field=models.ImageField(height_field=100, upload_to='img', width_field=100),
        ),
    ]