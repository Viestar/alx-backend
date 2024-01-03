#!/usr/bin/env python3
"""
This module contains an implementation of an LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU Cache implemention"""

    def __init__(self):
        """Constructor and inherits the super's dictionary """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        Adds an item into a cache
        Args:
            key(str): key of the item
            item: item to be added
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_data_list:
                self.cache_data_list.append(key)
            else:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped = self.cache_data_list.pop(0)
                del self.cache_data[popped]
                print("DISCARD: {}".format(popped))
    def get(self, key):
        """ Retrieves a cache item
        Args:
            key(str): key of the item to search
        Returns: None or an item."""
        if key:
            if key in self.cache_data:
                self.cache_data_list.remove(key)
                self.cache_data_list.append(key)
                return self.cache_data[key]
        return None
