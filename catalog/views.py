
from django.shortcuts import render


def produtos_list(request):
    return render(request, 'catalog/produtos_list.html')
