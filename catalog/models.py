# coding=utf-8

from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:category', kwargs={'slug': self.slug})


class Product(models.Model):
    name = models.CharField('Nome', max_length=100)
    slug = models.SlugField('Identificador', max_length=100)
    category = models.ForeignKey('catalog.Category', on_delete='Categoria')
    description = models.CharField('Descrição', max_length=200, blank=True)
    price = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    image = models.ImageField(
        'Imagem', upload_to='products', blank=True, null=True
    )
    image1 = models.ImageField(
        'Imagem1', upload_to='products', blank=True, null=True
    )
    image2 = models.ImageField(
        'Imagem2', upload_to='products', blank=True, null=True
    )

    tamanho = models.ManyToManyField('catalog.Tamanho')
    cor = models.ManyToManyField('catalog.Cor')

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    descricao_completa = models.TextField('Descrição Detalhes',blank=True,null=True)
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalog:product', kwargs={'slug': self.slug})




class Carroucel(models.Model):

    desc = models.CharField('Descrição', max_length=60)
    category = models.ForeignKey('catalog.Category', on_delete='Categoria')
    image = models.ImageField(
        'Imagem', upload_to='products'
    )

    class Meta:
        verbose_name = 'Carrocel'

    def __str__(self):
        return self.desc



class Tamanho(models.Model):
    tamanho = models.CharField('Tamanho', max_length=10)

    class Meta:
        verbose_name = 'Tamanho'
        verbose_name_plural = 'Tamanhos'


    def __str__(self):
        return self.tamanho


class Cor(models.Model):
    cor = models.CharField('Cor', max_length=20)

    class Meta:
        verbose_name = 'Cor'
        verbose_name_plural = 'Cores'

    def __str__(self):
        return self.cor



