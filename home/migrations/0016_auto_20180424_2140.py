# Generated by Django 2.0.1 on 2018-04-25 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_auto_20180425_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweets',
            name='ticker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.Coins'),
        ),
    ]
