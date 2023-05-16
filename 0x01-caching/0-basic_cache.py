#!/usr/bin/env python3
"""
Create a class BasicCache that inherits from
BaseCaching and is a caching system:
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    class inheritance in basecaching
    """

    def put(self, key, item):
        """
        key : element key
        item : element
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        key : element key
        """
        if key in self.cache_data.keys():
            return self.cache_data.get(key)
        return None
