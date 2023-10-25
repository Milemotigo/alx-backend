#!/usr/bin/env python3
'''
 a class FIFOCache that inherits from BaseCaching and is a caching system
'''


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ 
    a class FIFOCache that inherits from BaseCaching
    """
    def __init__(self):
       super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        if len(self.cache_data) >= self.MAX_ITEMS:
            first_data = next(iter(self.cache_data))
            print(f"DISCARD: {first_data}")
            del self.cache_data[first_data]

        self.cache_data[key] = item

    def get(self, key):
        if key is None:
            return None
        return self.cache_data.get(key, None)
