from .models import Item
from django.http import HttpResponse, JsonResponse
from celery.result import AsyncResult
from .tasks import get_similar_items_task
# Create your views here.


def index(request):
    return HttpResponse('<h1>App is running</h1>')


def get_all_items(request):
    item = Item()
    items = item.fetch_items()
    return JsonResponse({"items": items})


def get_platform_items(request, platform):
    item = Item()
    items = item.fetch_platform_items(platform)
    return JsonResponse({"items": items})


def get_one_item(request, query):
    item = Item()
    item.find(query)


def get_category_items(request, query):
    item = Item()
    items = item.fetch_category(query)
    return JsonResponse({"items": items})


def get_similar_items(request, title):
    item = Item()

    items = item.fetch_items()
    item_titles = [item['item_title'] for item in items]

    # call the get_similar_items_task asynchronously
    task = get_similar_items_task.delay(title)
    return JsonResponse({"task_id": task.id})


def get_task_info(request, task_id):
    task = AsyncResult(task_id)
    response_data = {
        'task_status': task.status,
        'task_id': task_id,
    }
    if task.ready():
        # Only include the result in the response if the task has finished
        response_data['task_result'] = task.result
        print(response_data)
    return JsonResponse(response_data)
