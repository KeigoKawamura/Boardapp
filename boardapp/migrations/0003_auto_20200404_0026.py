# Generated by Django 3.0.5 on 2020-04-04 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0002_auto_20200403_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
