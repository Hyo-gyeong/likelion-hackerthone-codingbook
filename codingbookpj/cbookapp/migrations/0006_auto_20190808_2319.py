# Generated by Django 2.2.4 on 2019-08-08 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbookapp', '0005_auto_20190808_2312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sharere',
            old_name='contents',
            new_name='recontents',
        ),
    ]