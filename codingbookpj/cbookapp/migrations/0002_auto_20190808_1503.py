# Generated by Django 2.2.4 on 2019-08-08 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cbookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sharecomment',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='sharere',
            options={'ordering': ['-id']},
        ),
    ]