# Generated by Django 3.0.8 on 2020-08-04 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='data',
            field=models.DateField(verbose_name='Data'),
        ),
    ]
