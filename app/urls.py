from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('product/<id>/',views.product,name="products"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('ind_product/<id>/',views.ind_product,name="ind_product"),
    path('glass_surface/<id>/',views.glass_surface,name="glass_surface")
]
