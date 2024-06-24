

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('shop/', views.shop, name='shop'),
    path("register/", views.register, name="register"),
    path('logout/', views.logout_view, name='logout')

]
