# Generated by Django 2.2 on 2021-04-19 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(max_length=500, upload_to='posts'),
        ),
        migrations.CreateModel(
            name='ProductDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('price', models.FloatField(default=0)),
                ('img', models.ImageField(upload_to='products')),
                ('img2', models.ImageField(upload_to='products')),
                ('img3', models.ImageField(upload_to='products')),
                ('description2', models.TextField(default='')),
                ('img4', models.ImageField(upload_to='products')),
                ('description3', models.TextField(default='')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Product')),
            ],
            options={
                'verbose_name': 'ProductDetail',
                'verbose_name_plural': 'ProductsDetail',
            },
        ),
    ]