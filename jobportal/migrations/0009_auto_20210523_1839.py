# Generated by Django 3.2 on 2021-05-23 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportal', '0008_auto_20210523_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='jobpost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
