# Generated by Django 2.2 on 2020-05-27 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_auto_20200527_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pics',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
