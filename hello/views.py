from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def contatos(request):
    return render(request, 'contatos.html')


def produtos_list(request):
    return render(request, 'produtos_list.html')


def produto(request):
    return render(request, 'produto.html')