#!/usr/bin/env python3
'''
a class BasicCache that inherits from BaseCaching and is a caching system
'''


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    basicCache class
    """
    def put(self, key, item):
        """
        Must assign to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data
        linked to key.
        """
        if key is None:
            return None
        return self.cache_data.get(key, None)
