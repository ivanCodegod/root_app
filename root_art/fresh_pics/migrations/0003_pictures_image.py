# Generated by Django 3.2.4 on 2021-07-06 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fresh_pics', '0002_alter_pictures_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pictures',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploaded_images', verbose_name='Фото'),
        ),
    ]
