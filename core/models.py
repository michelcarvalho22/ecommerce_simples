from django.db import models

# Create your models here.


class Empresa(models.Model):

    nome = models.CharField('Razão/Nome', max_length=60)
    fantasia = models.CharField('Fantasia', max_length=40, blank=True)
    # endereço
    cep = models.CharField('CEP', max_length=12, blank=True, null=True)
    endereco = models.CharField('Endereço', max_length=50, blank=True, null=True)
    numero = models.CharField('Nº', max_length=10, blank=True, null=True)
    complemento = models.CharField('Complemento', max_length=30, blank=True, null=True)
    bairro = models.CharField('Bairro', max_length=40, blank=True, null=True)
    cidade = models.CharField('Cidade', max_length=30, blank=True, null=True)
    uf = models.CharField('UF', max_length=2, blank=True, null=True)

    telefone = models.CharField('Telefone', max_length=30,null=True,blank=True)
    email = models.EmailField('Email',max_length=100,null=True,blank=True)

    descricao_empresa = models.CharField('Descrição Empresa', max_length=100,null=True,blank=True)

    link_facebook = models.CharField('Facebook', max_length=200,null=True,blank=True)
    link_twitter = models.CharField('Twitter', max_length=200, null=True, blank=True)
    link_instagran = models.CharField('Instagran', max_length=200, null=True, blank=True)
    link_linkedin = models.CharField('Linkedin', max_length=200, null=True, blank=True)


    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
        ordering = ['nome']

    def __str__(self):
        return self.nome

