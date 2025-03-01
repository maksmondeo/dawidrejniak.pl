from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('opinie', views.opinie, name='opinie'),
    path('polityka_prywatnosci', views.polityka_prywatnosci, name='polityka_prywatnosci'),
    path('odbierz', views.odbierz, name='odbierz'),
]
