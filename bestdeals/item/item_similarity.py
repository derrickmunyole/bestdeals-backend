from __future__ import absolute_import, unicode_literals
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
# assuming models.py and item_similarity.py are in the same directory
from .models import Item


class ItemSimilarity:
    def __init__(self, item):
        self.item = item

    def compute_similarities(self):
        items = self.item.fetch_items()
        item_titles = [item['item_title'] for item in items]

        # Create a TfidfVectorizer object
        tfidf = TfidfVectorizer().fit_transform(item_titles)

        # Compute the cosine similarity matrix
        cosine_sim = linear_kernel(tfidf, tfidf)

        return cosine_sim

    def get_similar_items(self, title):
        items = self.item.fetch_items()
        item_titles = [item['item_title'] for item in items]

        if title in item_titles:
            # Create a TfidfVectorizer object
            tfidf = TfidfVectorizer().fit_transform(item_titles)

            # Compute the cosine similarity matrix
            cosine_sim = linear_kernel(tfidf, tfidf)

            # Get the index of the item that matches the title
            idx = item_titles.index(title)

            # Get the pairwsie similarity scores of all items with that item
            sim_scores = list(enumerate(cosine_sim[idx]))

            # Sort the items based on the similarity scores
            sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

            # Get the scores of the 10 most similar items
            sim_scores = sim_scores[1:11]
        else:
            print(f"Title '{title}' not found in item_titles")

        # Get the item indices
        item_indices = [i[0] for i in sim_scores]

        # Return the top 10 most similar items
        return [items[i] for i in item_indices]
