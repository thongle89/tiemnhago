# Generated by Django 3.1.1 on 2020-10-25 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DanhMuc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.CharField(default='', max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock', models.BooleanField(max_length=25)),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('brief', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='details.danhmuc')),
            ],
        ),
    ]
