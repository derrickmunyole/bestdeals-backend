from django.urls import path
from .views import ReviewView, ItemReviewsView

urlpatterns = [
    path('reviews/user/<int:user_id>/',
         ReviewView.as_view(), name='user_reviews'),
    path('reviews/review/<int:review_id>/',
         ReviewView.as_view(), name='review_detail'),
    path('reviews/item/<int:item_id>/',
         ItemReviewsView.as_view(), name='item_reviews'),
]
