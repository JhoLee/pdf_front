# Generated by Django 3.0.3 on 2020-05-13 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mask', '0005_auto_20200513_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='result_image',
            field=models.ImageField(null=True, upload_to='mask/%Y/%m/%d'),
        ),
    ]
