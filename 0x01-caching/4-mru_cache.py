#!/usr/bin/env python3
"""MRU Caching"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """
    a class MRUCache that inherits from BaseCaching
    and is a caching system
    """
    def __init__(self):
        super().__init__()
        # Initialize an empty ordered dictionary
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """add to the cache by key, value"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            mru = next(reversed(self.cache_data))
            print(f"DISCARD: {mru}")
            del self.cache_data[mru]
        self.cache_data[key] = item

    def get(self, key):
        """
        fetch data by their key
        """
        if key is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
            return self.cache_data.get(key)
        else:
            return None
