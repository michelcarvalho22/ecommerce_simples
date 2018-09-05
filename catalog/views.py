# coding=utf-8

from django.shortcuts import render, get_object_or_404
from django.views import generic

from django.db import models
from django.views.decorators.cache import cache_page

# from watson import search as watson

from .models import Product, Category,Carroucel


def product_list(request):

    template_name = 'catalog/product_list.html'

    product = Product.objects.all()
    caroucel = Carroucel.objects.all()

    context = {
        'products' : product,
        'caroucel': caroucel
    }



    return render(request, template_name, context)






class CategoryListView(generic.ListView):

    template_name = 'catalog/category.html'
    context_object_name = 'product_list'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Category, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()


# @cache_page(60 * 10)
def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'catalog/product.html', context)
