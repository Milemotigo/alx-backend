#!/usr/bin/env python3
""" LRU Caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    a class LRUCache that inherits from
    BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Must assign to the dictionary
        self.cache_data the item value for the key key
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_item = next(iter(self.cache_data))
            print(f"DISCARD: {lru_item}")
            del self.cache_data[lru_item]
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
