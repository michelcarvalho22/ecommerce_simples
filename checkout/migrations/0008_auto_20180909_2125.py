# Generated by Django 2.0.2 on 2018-09-10 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0007_auto_20180909_2117'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='cor',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Cor'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='tamanho',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Tamanho'),
        ),
    ]