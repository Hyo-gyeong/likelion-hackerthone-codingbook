# Generated by Django 2.2.2 on 2019-08-09 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbookapp', '0008_auto_20190809_2138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cbookapp.CodeShare'),
        ),
    ]
