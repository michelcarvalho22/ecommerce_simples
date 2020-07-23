from django.db import models
from django.urls import reverse


class Greeting(models.Model):
<<<<<<< HEAD
    when = models.DateTimeField('date created', auto_now_add=True)


class Promocao(models.Model):

    name = models.CharField('Nome', max_length=100)

    created = models.DateTimeField('Criado em', auto_now_add=True)
    modified = models.DateTimeField('Modificado em', auto_now=True)

    class Meta:
        verbose_name = 'Promocao'
        verbose_name_plural = 'Promocoes'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('hello:index', kwargs={'slug': self.slug})
=======
    when = models.DateTimeField("date created", auto_now_add=True)
>>>>>>> 9a41ac0e2988172bbf5e17295857bc863053ce8a
