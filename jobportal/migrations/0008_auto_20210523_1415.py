# Generated by Django 2.2 on 2021-05-23 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0007_applyjob_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='document',
            field=models.FileField(upload_to=''),
        ),
    ]
