from django.urls import path
from .views import FavoriteView

urlpatterns = [
    path('', FavoriteView.as_view(), name='favorites'),
    path('<str:item_id>/', FavoriteView.as_view(), name='favorite_item'),
]
