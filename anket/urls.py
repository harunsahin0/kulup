from django.urls import path
from . import views

urlpatterns = [
    path('', views.anket_view, name='anket'),
    path('liste/', views.liste_view, name='liste'),
]