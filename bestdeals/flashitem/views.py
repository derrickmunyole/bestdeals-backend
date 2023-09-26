from .models import FlashItem
from django.http import HttpResponse, JsonResponse
# Create your views here.


def index(request):
    return HttpResponse("<h1>App is running<h1>")


def get_all_flash_items(request):
    flashitem = FlashItem()
    items = flashitem.fetch_items()
    print(type(items))
    print(items)
    return JsonResponse({'items': items}, safe=False)
