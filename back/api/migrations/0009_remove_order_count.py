# Generated by Django 2.2 on 2021-04-21 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='count',
        ),
    ]