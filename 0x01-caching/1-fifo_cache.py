#!/usr/bin/env python3
""" Module that contains class FIFOCache that inherits from BaseCache. """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ The Sub class of the BaseCaching class """
    def __init__(self):
        """class constructor inhrits dict from Base class """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """
        add item into a cache
        Args:
            key(str): key of the item to add
            item: item to add
        Returns: None
        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.cache_data_list[0])
                deleted = self.cache_data_list.pop(0)
                print(f"DISCARD: {deleted}")

    def get(self, key):
        """
        Retrieves an item from cache
        Args:
            key(str): key of the item to add
        Returns: None or item.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
