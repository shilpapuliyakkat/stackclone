# Generated by Django 4.1.3 on 2023-02-17 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stack', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='image',
        ),
    ]
