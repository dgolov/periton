# Generated by Django 3.1.4 on 2020-12-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20201225_1019'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.CharField(blank=True, db_index=True, max_length=250, null=True, verbose_name='Ссылка'),
        ),
    ]
