#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from
BaseCaching and is a caching system:
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    inheritance basecaching
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        key : element key
        item : element
        """
        if key and item:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                res = list(sorted(self.cache_data.keys()))[0]
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
