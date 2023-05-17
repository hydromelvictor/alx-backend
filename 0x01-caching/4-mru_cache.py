#!/usr/bin/env python3
"""
Create a class MRUCache that inherits from
BaseCaching and is a caching system:
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    inheritance
    """
    def __init__(self):
        super().__init__()
        self.old = {}

    def put(self, key, item):
        """
        key : element key
        item : element
        """
        if key and item:
            size = len(self.cache_data)
            if size >= BaseCaching.MAX_ITEMS:
                if key not in self.cache_data:
                    res = sorted(self.old.items(),
                                 key=lambda t: t[1][1])[size - 1]
                    del self.cache_data[res[0]]
                    del self.old[res[0]]
                    print("DISCARD: {}".format(res[0]))
            self.cache_data[key] = item
            self.old[key] = (item, datetime.now())

    def get(self, key):
        """
        key : element key
        """
        if key in self.cache_data.keys():
            self.old[key] = (self.old[key], datetime.now())
            return self.cache_data.get(key)
        return None
