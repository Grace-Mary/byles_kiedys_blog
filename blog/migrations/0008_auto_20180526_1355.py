# Generated by Django 2.0.5 on 2018-05-26 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180526_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='image.png', upload_to='images/'),
        ),
    ]