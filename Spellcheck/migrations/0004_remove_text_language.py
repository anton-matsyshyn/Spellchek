# Generated by Django 2.0.5 on 2018-05-28 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Spellcheck', '0003_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='text',
            name='language',
        ),
    ]
