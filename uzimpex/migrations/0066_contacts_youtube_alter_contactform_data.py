# Generated by Django 5.0.8 on 2022-09-21 12:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0065_delete_projects_remove_contacts_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='youtube',
            field=models.CharField(default='exit', max_length=200, verbose_name='Youtube '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactform',
            name='data',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2024, 9, 21, 17, 40, 5, 254593), null=True, verbose_name='Получено'),
        ),
    ]
