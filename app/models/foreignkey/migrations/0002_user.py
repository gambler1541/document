# Generated by Django 2.0.6 on 2018-06-18 02:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foreignkey', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='foreignkey.User')),
            ],
        ),
    ]
