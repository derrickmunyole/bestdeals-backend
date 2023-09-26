from django.http import JsonResponse
from .tasks import trigger_scrape_task


def trigger_scrape(request):
    # Trigger your scraping task here
    query = request.GET.get('query')
    print(f"Query in Django view: {query}")
    trigger_scrape_task.delay(query)
    return JsonResponse({'status': 'Scraping started'})
