# Generated by Django 2.0.2 on 2018-08-30 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product_carroucel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='descricao_completa',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição Detalhes'),
        ),
    ]
