#!/usr/bin/env python3
""" Module that contains class FIFOCache that inherits from BaseCache. """
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ Allows storing and retrieving items from a dictionary with a LFU
    removal mechanism when the limit is reached.
    """

    def __init__(self):
        """ Cache Initialisation. """
        super().__init__()
        self.cache_data = OrderedDict()
        self.keys_frequency = []

    def __reorder_items(self, mru_key):
        """ Re-orders the items in this cache based on the most recently
          used item.
        """

        ins_position = 0
        max_positions = []
        mru_frequency = 0
        mru_position = 0
        for i, key_frequency in enumerate(self.keys_frequency):
            if key_frequency[0] == mru_key:
                mru_frequency = key_frequency[1] + 1
                mru_position = i
                break
            elif len(max_positions) == 0:
                max_positions.append(i)
            elif key_frequency[1] < self.keys_frequency[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for pos in max_positions:
            if self.keys_frequency[pos][1] > mru_frequency:
                break
            ins_position = pos
        self.keys_frequency.pop(mru_position)
        self.keys_frequency.insert(ins_position, [mru_key, mru_frequency])

    def put(self, key, item):
        """CAche Additions. """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_frequency[-1]
                self.cache_data.pop(lfu_key)
                self.keys_frequency.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            ins_index = len(self.keys_frequency)
            for i, key_frequency in enumerate(self.keys_frequency):
                if key_frequency[1] == 0:
                    ins_index = i
                    break
            self.keys_frequency.insert(ins_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)
