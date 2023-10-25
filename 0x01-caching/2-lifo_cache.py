#!/usr/bin/env python3
''' LIFO Caching
'''

from base_caching import BaseCaching

class LIFOCache(BaseCaching):

    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            for k, v in self.cache_data.items():
                last_key = k[-1]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]
        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return self.cache_data.get(key, None)
        