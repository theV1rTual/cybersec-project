# Generated by Django 2.2 on 2021-04-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210419_2057'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='canvas',
            options={'verbose_name': 'Canvas', 'verbose_name_plural': 'Canvases'},
        ),
        migrations.RemoveField(
            model_name='product',
            name='post',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=200),
        ),
    ]
