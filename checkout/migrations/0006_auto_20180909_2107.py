# Generated by Django 2.0.2 on 2018-09-10 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20180213_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='cor',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cor'),
        ),
        migrations.AddField(
            model_name='cartitem',
            name='tamanho',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tamanho'),
        ),
    ]
