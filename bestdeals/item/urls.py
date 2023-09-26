from django.urls import path
from . import views
from .views import get_task_info


urlpatterns = [
    path("", views.index),
    path("get_items", views.get_all_items),
    path('get_category_items/<str:query>', views.get_category_items),
    path("get_one", views.get_one_item),
    path('platform_items/<str:platform>', views.get_platform_items),
    path('similar_items/<str:title>', views.get_similar_items),
    path('task-info/<str:task_id>/', get_task_info, name='task_info'),
]
