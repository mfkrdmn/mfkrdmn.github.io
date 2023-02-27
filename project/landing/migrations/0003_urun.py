# Generated by Django 3.2.9 on 2023-02-27 19:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_rfq'),
    ]

    operations = [
        migrations.CreateModel(
            name='urun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim_tr', models.CharField(max_length=200, verbose_name='İsim Türkçe')),
                ('isim_en', models.CharField(max_length=200, verbose_name='İsim Türkçe')),
                ('isim_de', models.CharField(max_length=200, verbose_name='İsim Türkçe')),
                ('isim_ar', models.CharField(max_length=200, verbose_name='İsim Türkçe')),
                ('hakkimizda_tr', ckeditor.fields.RichTextField(verbose_name='Hakkımızda Yazısı Türkçe')),
                ('hakkimizda_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Hakımızda Yazısı İngilizce')),
                ('hakkimizda_de', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Hakımızda Yazısı Almanca')),
                ('hakkimizda_ar', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Hakımızda Yazısı Almanca')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cvfoto/', verbose_name='Size Ait Olan Resmi Ekleyin')),
            ],
        ),
    ]
