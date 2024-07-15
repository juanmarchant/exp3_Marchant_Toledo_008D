
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import ResetPasswordView, CustomPasswordResetConfirmView

urlpatterns = [
    path('', views.index, name='index'),

    #USER
    path('profile/', views.profile, name='profile'),

    # PASSWORD
    path('password-reset/', ResetPasswordView.as_view(template_name='registration/password_reset.html'), name='password_resett'),
    path('accounts/reset/<uidb64>/<token>/',
         CustomPasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    # /accounts/reset/MQ/ca6ser-7c48c994ed5c248ecfb3019c623c6fc4/
    # CRUD
    path('add/', views.add, name="add"),
    path('products/', views.products, name='products'),
    path('details/<id>/', views.details, name="details"),
    path('modify/<id>/', views.modify, name="modify"),
    path('deleteProd/<id>/', views.delete, name="deleteProd"),
    # SEARCH
    path('search/', views.search, name='search'),
    # ORDERS
    path('orders/', views.orders, name='orders'),
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
