# Generated by Django 4.2.6 on 2024-04-16 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_userotp_action_userotp_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='address_type',
            field=models.SmallIntegerField(choices=[(0, 'Apartment'), (1, 'Home'), (2, 'Office')], default=1, verbose_name='Address Type'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Apartment Number'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='block_number',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Block Number'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='building_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Building Name'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='building_number',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Building Number'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='floor_number',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Floor Number'),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='street_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Street Name'),
        ),
    ]