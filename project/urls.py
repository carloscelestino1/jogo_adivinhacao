from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('game.urls')),  # Inclui as URLs do jogo
]

