# Generated by Django 2.0.5 on 2018-05-26 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180526_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(default='', null=True, upload_to='images/'),
        ),
    ]