# Generated by Django 3.0.3 on 2020-05-13 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mask', '0002_auto_20200513_1835'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='author',
            field=models.CharField(default='unkown', max_length=10),
            preserve_default=False,
        ),
    ]
