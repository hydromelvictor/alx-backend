#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from
BaseCaching and is a caching system:
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """inheritance"""

    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        """
        key : element key
        item : element
        """
        old = self.cache_data.copy()
        if key and item:
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS:
                for k, v in self.cache_data.items():
                    if k in old and v != old[k]:
                        del old[k]
                if key not in self.cache_data:
                    res = sorted(old.keys())[0]
                    del self.cache_data[res]
                    print("DISCARD: {}".format(res))
            self.cache_data[key] = item
    
    def get(self, key):
        """
        key : element key
        """
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None