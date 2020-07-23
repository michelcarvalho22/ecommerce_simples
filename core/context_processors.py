# coding=utf-8

from .models import Empresa


def empresa(request):
    return {
        'empresa' : Empresa.objects.get()
    }
