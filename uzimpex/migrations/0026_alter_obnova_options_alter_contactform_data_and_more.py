# Generated by Django 4.0.3 on 2022-04-04 09:51

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0025_obnova_otdeli_ruk_vacansiya_alter_contactform_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='obnova',
            options={'verbose_name': '2.4 Объявления', 'verbose_name_plural': '2.4 Объявления'},
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 4, 4, 14, 51, 54, 409940), null=True, verbose_name='Получено'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Slider description'),
        ),
        migrations.AlterField(
            model_name='obnova',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='otdeli',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='plans',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='ruk',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='vacansiya',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
