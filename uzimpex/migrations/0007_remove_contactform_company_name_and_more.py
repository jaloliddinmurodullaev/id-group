# Generated by Django 4.0.2 on 2022-02-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzimpex', '0006_alter_contactform_options_alter_contacts_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactform',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='contactform',
            name='date',
        ),
        migrations.RemoveField(
            model_name='contactform',
            name='name',
        ),
        migrations.AddField(
            model_name='contacts',
            name='map',
            field=models.CharField(max_length=10000, null=True, verbose_name='Карта'),
        ),
    ]
