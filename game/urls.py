from django.urls import path
from . import views

urlpatterns = [
    path('', views.iniciar_jogo, name='iniciar_jogo'),
    path('jogar/', views.jogar, name='jogar'),
]
