from django.urls import path

from menu import views

app_name = 'menu'

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/', views.product, name='product')
]
