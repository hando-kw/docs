# Generated by Django 4.2.6 on 2024-04-13 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_useraddress_additional_information'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='fullname',
        ),
    ]
