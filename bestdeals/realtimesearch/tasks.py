from celery import shared_task
from run import run_custom_jumiaitems_bot, run_custom_kiliitems_bot


@shared_task
def trigger_scrape_task(query):
    print(f"Query in Celery task: {query}")
    kiliitems = run_custom_kiliitems_bot(query)
    jumiaitems = run_custom_jumiaitems_bot(query)
    return kiliitems + jumiaitems
