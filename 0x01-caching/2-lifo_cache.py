#!/usr/bin/env python3
''' LIFO Caching
'''

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    a class LIFOCache that inherits from BaseCaching
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        You must use self.cache_data - dictionary
        from the parent class BaseCaching
        """
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # last_key = list(self.cache_data.keys())[-1]
            for k, _ in self.cache_data.items():
                last_key = k[-1]
            print(f"DISCARD: {last_key}")
            del self.cache_data[last_key]
        self.cache_data[key] = item

    def get(self, key):
        """
        Must return the value in self.cache_data linked to key
        """
        if key is None:
            return self.cache_data.get(key, None)
