from django.urls import path
from . import views

urlpatterns = [
    path('exercise', views.exercise, name='exercise'),
    path('', views.index, name='index'),
]
