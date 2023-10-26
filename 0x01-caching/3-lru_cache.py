#!/usr/bin/env python3
"""
3. LRU Caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    a class LRUCache that inherits from BaseCaching
    and is a caching system
    """

    def __init__(self):
        super().__init__()
        """
        It ensures that the initialization code in the parent
        class is executed before any additional initialization
        specific to the child class
        """
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        A method that helps to add item to the cache
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru = next(iter(self.cache_data))
            print(f"DISCARD: {lru}")
            del self.cache_data[lru]
        self.cache_data[key] = item

    def get(self, key):
        """
        Used to get the item with a specific key
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=True)
            return self.cache_data.get(key)
        else:
            return None

