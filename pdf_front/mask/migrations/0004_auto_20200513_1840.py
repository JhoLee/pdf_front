# Generated by Django 3.0.3 on 2020-05-13 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mask', '0003_request_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='mod_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]