from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Favorites
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
logger = logging.getLogger(__name__)


@method_decorator(csrf_exempt, name='dispatch')
class FavoriteView(View):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.favorite = Favorites()
        self.item_id = None

    def dispatch(self, request, *args, **kwargs):
        self.item_id = kwargs.get('item_id')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        if 'item_id' in kwargs:
            return self.remove_favorite(kwargs['item_id'])
        else:
            return self.get_all_favorite_items(request)

    def post(self, request, *args, **kwargs):
        return self.add_to_favorite(request)

    def delete(self, request, *args, **kwargs):
        print(kwargs)
        item_id = kwargs.get('item_id')
        if item_id:
            return self.remove_favorite(self.item_id)
        else:
            return self.remove_favorites()

    def get_all_favorite_items(self, request):
        try:
            user_id = request.GET.get('user_id')
            items = self.favorite.fetch_favorites(user_id)
            logger.info(f"Fetched items: {items}")
            return JsonResponse({'items': items})
        except Exception as e:
            logger.error(f"An error occurred while fetching items: {e}")
            return JsonResponse({"error": str(e)}, status=500)

    def add_to_favorite(self, request):
        try:
            favorite_item = json.loads(request.body)
            added_item = self.favorite.add_favorite(favorite_item)
            return JsonResponse(added_item)
        except Exception as e:
            logger.error(f"An error occurred while adding a favorite: {e}")
            return JsonResponse({"error": str(e)}, status=500)

    def remove_favorite(self, item_id):
        print(item_id)
        try:
            deleted_count = self.favorite.remove_item(item_id)
            if deleted_count > 0:
                return JsonResponse({"Deleted Item": item_id})
            else:
                return JsonResponse({"error": "No item found with the given id"}, status=404)
        except Exception as e:
            logger.error(f"An error occurred while removing an item: {e}")
            return JsonResponse({"error": str(e)}, status=500)

    def remove_favorites(self):
        try:
            removed_items = self.favorite.remove_items()
            return JsonResponse({"Deleted Count": removed_items})
        except Exception as e:
            logger.error(f"An error occurred while removing items: {e}")
            return JsonResponse({"error": str(e)}, status=500)
