from django.views import View
from django.http import JsonResponse
from .models import Review


class ReviewView(View):
    def get(self, request, user_id):
        review = Review()
        reviews = review.fetch_reviews(user_id)
        if reviews is not None:
            return JsonResponse(reviews, safe=False)
        else:
            return JsonResponse({"error": "An error occurred while fetching reviews"}, status=500)

    def post(self, request):
        review = Review()
        new_review = request.POST
        result = review.add_review(new_review)
        if "error" not in result:
            return JsonResponse(result, status=201)
        else:
            return JsonResponse(result, status=500)

    def put(self, request, review_id):
        review = Review()
        updated_review = request.POST
        result = review.update_review(review_id, updated_review)
        if "error" not in result:
            return JsonResponse({"message": "Review updated successfully"}, status=200)
        else:
            return JsonResponse(result, status=500)

    def delete(self, request, review_id):
        review = Review()
        review.remove_review(review_id)
        return JsonResponse({"message": "Review deleted successfully"}, status=200)


# Class view for fetching all reviews of a particular item
class ItemReviewsView(View):
    def get(self, request, item_id):
        review = Review()
        reviews = review.fetch_reviews(item_id)
        if reviews is not None:
            return JsonResponse(reviews, safe=False)
        else:
            return JsonResponse({"error": "An error occurred while fetching reviews"}, status=500)
