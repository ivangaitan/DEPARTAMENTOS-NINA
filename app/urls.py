from django.urls import path
from . import views

urlpatterns = [
    path('', views.mostrar_inicio, name="home"),
    path('departamentos/', views.mostrar_departamentos, name="departamentos"),
    path('seleccionado/<int:pk>/', views.mostrar_seleccionado, name="seleccionado"),
]

