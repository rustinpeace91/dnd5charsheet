# Generated by Django 2.0.2 on 2019-02-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0003_remove_character_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='image',
            field=models.ImageField(default='images/knight.png', upload_to=''),
        ),
    ]