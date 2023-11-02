from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
    path('theory/', views.theory, name='theory'),
    path('e_greedy/', views.e_greedy, name='e-greedy'),
    path('greedy/', views.greedy, name='greedy'),
    path('ucb/', views.ucb, name='ucb'),
]