from django.http import JsonResponse
from django.views import View
from .models import SearchItem


class SearchView(View):
    def get(self, request, *args, **kwargs):
        query = request.GET.get('q', '')
        search_item = SearchItem()
        results = search_item.search(query)
        return JsonResponse({'results': results})
