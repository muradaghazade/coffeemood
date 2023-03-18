from django.urls import path
from core.views import *

app_name = 'core'


urlpatterns = [
    path('',MainPageView.as_view(),name ='main'),
    path('categories/en/',EngCategoriesView.as_view(),name ='category-en'),
    path('categories/ru/',RuCategoriesView.as_view(),name ='category-ru'),
    path('categories/az/',AzCategoriesView.as_view(),name ='category-az'),
    path('products/en/',EngProductsView.as_view(),name ='products-en'),
    path('products/ru/',RuProductsView.as_view(),name ='products-ru'),
    path('products/az/',AzProductsView.as_view(),name ='products-az'),
]