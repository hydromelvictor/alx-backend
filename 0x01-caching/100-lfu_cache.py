#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system:
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """inheritance"""

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
                    res_dict = dict(sorted(self.old.items(), key=lambda t: t[1][2]))
                    res = sorted(res_dict.items(), key=lambda t: t[1][2])[0]
                    del self.cache_data[res[0]]
                    del self.old[res[0]]
                    print("DISCARD: {}".format(res[0]))
            self.cache_data[key] = item
            self.old[key] = (item, datetime.now(), 0 if key not in self.old.keys() else self.old[key][2] + 1)

    def get(self, key):
        """
        key : element key
        """
        if key in self.cache_data.keys():
            self.old[key] = (self.old[key], datetime.now(), self.old[key][2] + 1)
            return self.cache_data.get(key)
        return None
