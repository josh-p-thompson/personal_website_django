# Generated by Django 3.0 on 2019-12-09 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('sub_title_1', models.CharField(max_length=300)),
                ('content_1', models.TextField()),
                ('sub_title_2', models.CharField(max_length=300)),
                ('content_2', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('sub_title', models.CharField(max_length=300)),
                ('link', models.CharField(max_length=300)),
                ('image', models.ImageField(upload_to='apps/core/static/images/')),
            ],
        ),
    ]
