

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # CRUD
    path('products', views.products, name='products'),
    path('details/<id>/', views.details, name="details"),
    path('modify/<id>/', views.modify, name="modify"),
    path('deleteProd/<id>/', views.delete, name="deleteProd"),
    # NORMAL VIEW
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path("register/", views.register, name="register"),
    path('logout/', views.logout_view, name='logout'),
    path('agregar/<id>', views.agregar_producto, name="agregar"),
    path('restar/<id>', views.restar_producto, name="restar"),
    path('limpiar/', views.limpiar_producto, name="limpiar"),
    path('generarBoleta/', views.generarBoleta,name="generarBoleta"),
]
