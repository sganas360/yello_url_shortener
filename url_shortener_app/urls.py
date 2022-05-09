from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("encode", views.encode, name="encode"),
    path("decode" , views.decode, name="decode"),
]
