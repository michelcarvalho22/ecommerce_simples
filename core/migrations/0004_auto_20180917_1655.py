# Generated by Django 2.0.2 on 2018-09-17 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_empresa_descricao_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='link_facebook',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='link_instagran',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Instagran'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='link_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Linkedin'),
        ),
        migrations.AddField(
            model_name='empresa',
            name='link_twitter',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Twitter'),
        ),
    ]
