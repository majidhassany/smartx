# Generated by Django 2.2 on 2020-05-27 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0006_userprofileinfo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofileinfo',
            old_name='profile_pic',
            new_name='profile_pics',
        ),
    ]