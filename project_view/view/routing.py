from django.urls import path 

from .consumers import WSConsumer

ws_urlpattern = [
    path('ws/main', WSConsumer.as_asgi())
]