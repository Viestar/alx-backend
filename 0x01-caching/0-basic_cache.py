#!/usr/bin/env python3
"""
Module contains class BasicCache that inherits from BaseCaching.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ basic caching system """
    def __init__(self):
        """ initialize class instance """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Adds an item to the caching system
        Args:
            key(str): key of the item.
            item(str): item to add.
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ return the value in self.cache_data linked to key. """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
