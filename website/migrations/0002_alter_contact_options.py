# Generated by Django 3.2.12 on 2022-05-04 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ('created_date',)},
        ),
    ]
