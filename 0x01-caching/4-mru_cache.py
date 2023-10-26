#!/usr/bin/env python3
"""Task 4: MRU Caching.
"""
from collections import OrderedDict

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """A class `MRUCache` that inherits
       from `BaseCaching` and is a caching system
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                mru_key, _ = self.cache_data.popitem(False)
                print("DISCARD:", mru_key)
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=False)
        else:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)

# #!/usr/bin/env python3
# """MRU Caching"""

# from base_caching import BaseCaching
# from collections import OrderedDict


# class MRUCache(BaseCaching):
#     """
#     a class MRUCache that inherits from BaseCaching
#     and is a caching system
#     """
#     def __init__(self):
#         """
#         Initialize the cache
#         """
#         super().__init__()
#         # Initialize an empty ordered dictionary
#         self.cache_data = OrderedDict()

#     def put(self, key, item):
#         """
#         add to the cache by key, value
#         if key is None or item is None return None
#         """
#         if key is None or item is None:
#             return
#         if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
#             mru = next(reversed(self.cache_data))
#             print(f"DISCARD: {mru}")
#             del self.cache_data[mru]
#         self.cache_data[key] = item
#         self.cache_data.move_to_end(key, last=False)

#     def get(self, key):
#         """
#         fetch data by their key
#         return the value in self.cache_data linked to key
#         """
#         if key is None:
#             return None
#         if key in self.cache_data:
#             self.cache_data.move_to_end(key, last=False)
#             return self.cache_data.get(key)
#         else:
#             return None
