# Generated by Django 3.0.8 on 2020-08-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200804_1658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados',
            name='vlquota',
            field=models.DecimalField(decimal_places=7, max_digits=15, verbose_name='Valor Quota'),
        ),
    ]