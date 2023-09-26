from celery import shared_task
from celery.utils.log import get_task_logger
from .item_similarity import ItemSimilarity
from .models import Item


logger = get_task_logger(__name__)


@shared_task
def get_similar_items_task(title):
    item_similarity = ItemSimilarity(Item())
    similar_items = item_similarity.get_similar_items(title)
    return similar_items
