from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView
from core.models import Category, Product

class MainPageView(TemplateView):
    template_name = "index.html"

class EngCategoriesView(ListView):
    template_name = "categories.html"
    model = Category
    context_object_name = 'categories'

class RuCategoriesView(ListView):
    template_name = "ru_categories.html"
    model = Category
    context_object_name = 'categories'

class AzCategoriesView(ListView):
    template_name = "az_categories.html"
    model = Category
    context_object_name = 'categories'

class EngProductsView(ListView):
    template_name = "list.html"
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        category = self.request.GET.get('category')
        queryset = Product.objects.order_by('-id')

        if category:
            queryset = queryset.filter(category__en_title=category)
        return queryset
    
class RuProductsView(ListView):
    template_name = "ru_list.html"
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        category = self.request.GET.get('category')
        queryset = Product.objects.order_by('-id')

        if category:
            queryset = queryset.filter(category__ru_title=category)
        return queryset

class AzProductsView(ListView):
    template_name = "az_list.html"
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
    
    def get_queryset(self):
        category = self.request.GET.get('category')
        queryset = Product.objects.order_by('-id')

        if category:
            queryset = queryset.filter(category__az_title=category)
        return queryset
