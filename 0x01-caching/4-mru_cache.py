#!/usr/bin/env python3
""" Module that contains MRUCache that inherits from BaseCaching """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRU Caching System"""

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
            if key not in self.cache_data_order:
                self.cache_data_order.append(key)
            else:
                self.cache_data_order.remove(key)
                self.cache_data_order.append(key)
            if len(self.cache_data_order) > BaseCaching.MAX_ITEMS:
                length_c = len(self.cache_data_order)
                popped = self.cache_data_order.pop(length_c - 2)
                del self.cache_data[popped]
                print("DISCARD: {}".format(str(popped)))

    def get(self, key):
        """ Retrieves a cache item
        Args:
            key(str): key of the item to search
        Returns: None or an item.
        """
        if key in self.cache_data:
            self.cache_data_order.remove(key)
            self.cache_data_order.append(key)
            return self.cache_data[key]
        return None
