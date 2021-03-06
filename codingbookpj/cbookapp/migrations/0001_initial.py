# Generated by Django 2.2.4 on 2019-08-07 16:28

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CodeAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='askimage/')),
                ('body', models.TextField()),
                ('codes', models.TextField(default='코드 없음')),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('subject', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CodeShare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shareimage/')),
                ('body', models.TextField()),
                ('codes', models.TextField(default='코드 없음')),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('subject', models.CharField(max_length=50)),
                ('university', models.CharField(default='없음', max_length=50)),
                ('score', models.CharField(default='없음', max_length=50)),
                ('writer', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ShareComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=200)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='cbookapp.CodeShare')),
            ],
        ),
        migrations.CreateModel(
            name='ShareRe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=200)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='cbookapp.ShareComment')),
            ],
        ),
    ]
