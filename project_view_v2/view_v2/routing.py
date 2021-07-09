from django.urls import path 

from .consumers import WSConsumer

ws_urlpatterns = {
    path('ws/msg', WSConsumer.as_asgi())
}