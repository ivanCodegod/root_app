# Generated by Django 3.2.4 on 2021-07-06 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_pics', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pictures',
            options={'verbose_name': 'Новая картина', 'verbose_name_plural': 'Новые картины'},
        ),
    ]
