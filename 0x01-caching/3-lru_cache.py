#!/usr/bin/env python3
""" LRU Caching
"""

from base_caching import BaseCaching
from collections import OrderedDict

class LRUCache(BaseCaching):

    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict
    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            print(f"DISCARD: {self.cache_data[key]}")
            self.cache_data.popitem(last=False)
    
    def get(self, key):
        if key is None:
            return self.cache_data(key, None)
