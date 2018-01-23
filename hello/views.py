from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contatos(request):
    return render(request, 'contatos.html')


def produto(request):
    return render(request, 'produto.html')
