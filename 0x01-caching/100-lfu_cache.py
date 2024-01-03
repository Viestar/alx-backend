#!/usr/bin/env python3
""" Module that contains class FIFOCache that inherits from BaseCache. """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    def __init__(self):
        super().__init__()
        self.frequency = {}  # Dictionary to store the frequency of each key

    def put(self, key, item):
        if key is None or item is None:
            return

        # Update the frequency of the key
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

        # Assign the item value to the key in cache_data
        self.cache_data[key] = item

        # Check if the number of items exceeds MAX_ITEMS
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Find the key(s) with the minimum frequency
            min_frequency = min(self.frequency.values())
            keys_to_discard = [
                k for k, v in self.frequency.items() if v == min_frequency]

            if len(keys_to_discard) > 1:
                lru_key = min(self.access_time,
                              key=lambda k: self.access_time[k])
                keys_to_discard = [lru_key]

            # Discard the least frequency used item(s)
            for discard_key in keys_to_discard:
                del self.cache_data[discard_key]
                del self.frequency[discard_key]
                del self.access_time[discard_key]
                print(f"DISCARD: {discard_key}")

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        # Update the frequency and access time of the key
        self.frequency[key] += 1
        self.access_time[key] = self.current_time
        return self.cache_data[key]
