# Generated by Django 3.2.6 on 2021-08-23 00:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210819_1825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timeline',
            old_name='action',
            new_name='status',
        ),
    ]