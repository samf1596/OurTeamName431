# Generated by Django 2.0.1 on 2018-04-22 19:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20180421_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertransactions',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.UserProfile'),
        ),
    ]
