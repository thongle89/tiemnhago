# Generated by Django 3.1.1 on 2020-10-26 05:37

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
                ('code', models.CharField(max_length=3)),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SanPham',
            fields=[
                ('sku', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('stock', models.BooleanField(max_length=25)),
                ('image', models.ImageField(upload_to='%Y/%m/%d/')),
                ('brief', models.TextField(max_length=150)),
                ('description', models.TextField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='details.danhmuc')),
            ],
        ),
    ]
