# Generated by Django 2.0.2 on 2019-04-11 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0005_auto_20190228_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='weapon',
            name='effects',
            field=models.TextField(blank=True),
        ),
    ]
