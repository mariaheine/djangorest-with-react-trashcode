# Generated by Django 2.1.1 on 2018-09-27 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_en',
            field=models.TextField(default='empty'),
        ),
        migrations.AddField(
            model_name='article',
            name='content_pl',
            field=models.TextField(default='empty'),
        ),
        migrations.AddField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='header_en',
            field=models.TextField(default='empty'),
        ),
        migrations.AlterField(
            model_name='article',
            name='heade_pl',
            field=models.TextField(default='empty'),
        ),
    ]
