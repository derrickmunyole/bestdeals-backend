from django.urls import path
from .views import trigger_scrape

urlpatterns = [
    # ... your other url patterns ...
    path('trigger_scrape/', trigger_scrape, name='trigger_scrape'),
]
