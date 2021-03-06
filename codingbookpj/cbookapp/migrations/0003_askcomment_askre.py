# Generated by Django 2.2.4 on 2019-08-08 07:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cbookapp', '0002_auto_20190808_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('askcontents', models.CharField(max_length=200)),
                ('askpost', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='askcomments', to='cbookapp.CodeAsk')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='AskRe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('askcontents', models.CharField(max_length=200)),
                ('askcomment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='askreplies', to='cbookapp.AskComment')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
