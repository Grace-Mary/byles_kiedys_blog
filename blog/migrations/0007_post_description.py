# Generated by Django 2.0.5 on 2018-05-31 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20180531_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(default='Two-three sentences as a description'),
        ),
    ]
