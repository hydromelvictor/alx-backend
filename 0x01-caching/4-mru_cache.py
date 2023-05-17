#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from
BaseCaching and is a caching system:
"""
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    inheritance
    """
    def __init__(self):
        super().__init__()
    
    def put(self, key, item):
        """
        key : element key
        item : element
        """
        old = self.cache_data.copy()
        new = {}
        if key and item:
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS:
                new = {
                    k: v for k, v in self.cache_data.items()
                    if k in old.keys() and v != old[k]
                    }
                if key not in self.cache_data:
                    res = sorted(new.keys() if len(new) != 0 else old.keys())[0]
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