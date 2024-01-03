#!/usr/bin/env python3
""" Module that contains class FIFOCache that inherits from BaseCache. """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.cache_data_list = {}  # Dictionary to store the cache_data_list of each key

    def put(self, key, item):
        if key is None or item is None:
            return

        # Update the cache_data_list of the key
        if key in self.cache_data_list:
            self.cache_data_list[key] += 1
        else:
            self.cache_data_list[key] = 1

        # Assign the item value to the key in cache_data
        self.cache_data[key] = item

        # Check if the number of items exceeds MAX_ITEMS
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the key(s) with the minimum cache_data_list
            min_frequency = min(self.cache_data_list.values())
            keys_to_discard = [
                k for k, v in self.cache_data_list.items() if v == min_frequency]

            if len(keys_to_discard) > 1:
                lru_key = min(self.access_time,
                              key=lambda k: self.access_time[k])
                keys_to_discard = [lru_key]

            # Discard the least cache_data_list used item(s)
            for discard_key in keys_to_discard:
                del self.cache_data[discard_key]
                del self.cache_data_list[discard_key]
                del self.access_time[discard_key]
                print(f"DISCARD: {discard_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Update the cache_data_list and access time of the key
        self.cache_data_list[key] += 1
        self.access_time[key] = self.current_time
        return self.cache_data[key]
