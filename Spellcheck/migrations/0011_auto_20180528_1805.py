# Generated by Django 2.0.5 on 2018-05-28 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spellcheck', '0010_auto_20180528_1804'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='author',
        ),
        migrations.RemoveField(
            model_name='text',
            name='language',
        ),
    ]
