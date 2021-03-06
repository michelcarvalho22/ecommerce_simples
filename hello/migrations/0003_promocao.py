# Generated by Django 2.0.2 on 2018-02-24 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0002_auto_20180120_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Promocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products', verbose_name='Imagem')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Promocao',
                'verbose_name_plural': 'Promocoes',
                'ordering': ['name'],
            },
        ),
    ]
