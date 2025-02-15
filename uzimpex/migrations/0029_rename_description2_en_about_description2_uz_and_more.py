# Generated by Django 4.0.2 on 2022-04-06 12:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0028_about_description2_en_about_description2_ru_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='description2_en',
            new_name='description2_uz',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='description_en',
            new_name='description_uz',
        ),
        migrations.RenameField(
            model_name='about',
            old_name='title_en',
            new_name='title_uz',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='content_en',
            new_name='content_uz',
        ),
        migrations.RenameField(
            model_name='banner',
            old_name='title_en',
            new_name='title_uz',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='content_en',
            new_name='content_uz',
        ),
        migrations.RenameField(
            model_name='documents',
            old_name='title_en',
            new_name='title_uz',
        ),
        migrations.RenameField(
            model_name='obnova',
            old_name='description_en',
            new_name='description_uz',
        ),
        migrations.RenameField(
            model_name='otdeli',
            old_name='description_en',
            new_name='description_uz',
        ),
        migrations.RenameField(
            model_name='plans',
            old_name='description_en',
            new_name='description_uz',
        ),
        migrations.RenameField(
            model_name='plans',
            old_name='title_en',
            new_name='title_uz',
        ),
        migrations.RenameField(
            model_name='ruk',
            old_name='description_en',
            new_name='description_uz',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='description_en',
            new_name='description_uz',
        ),
        migrations.RenameField(
            model_name='services',
            old_name='title_en',
            new_name='title_uz',
        ),
        migrations.RenameField(
            model_name='vacansiya',
            old_name='description_en',
            new_name='description_uz',
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2022, 4, 6, 17, 45, 25, 568507), null=True, verbose_name='Получено'),
        ),
    ]
