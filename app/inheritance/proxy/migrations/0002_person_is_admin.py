# Generated by Django 2.0.6 on 2018-06-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proxy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]