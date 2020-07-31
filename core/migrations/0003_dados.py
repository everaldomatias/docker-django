# Generated by Django 2.2.13 on 2020-07-31 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_arquivos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', models.CharField(max_length=100, verbose_name='CNPJ')),
                ('data', models.DateTimeField(verbose_name='Data')),
                ('vltotal', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor Total')),
                ('vlquota', models.DecimalField(decimal_places=7, max_digits=15, verbose_name='Valor Quota')),
                ('vlpatrimliq', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Valor Pat Liq')),
                ('captcdia', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='Captc Dia')),
                ('resgdia', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Resgate Dia')),
                ('nrcotst', models.IntegerField(verbose_name='Nr Cotst')),
            ],
        ),
    ]