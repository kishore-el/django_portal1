# Generated by Django 2.2 on 2021-05-23 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0006_auto_20210523_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='applyjob',
            name='document',
            field=models.FileField(default=1, upload_to='documents/'),
            preserve_default=False,
        ),
    ]
