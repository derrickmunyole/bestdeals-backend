from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("get_flash_items", views.get_all_flash_items),
]
