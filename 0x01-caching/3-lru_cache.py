#!/usr/bin/env python3
""" LRUCache module """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and implements an LRU caching system """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()
        self.order = []  # Keep track of the order of keys

    def put(self, key, item):
        """ Add an item in the cache

        If the cache exceeds the MAX_ITEMS limit,
        the least recently used item is discarded.

        Args:
            key (str): The key under which the item should be stored.
            item (Any): The item to store in the cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.order.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD: {}".format(lru_key))

        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """ Get an item by key

        Args:
            key (str): The key to look up in the cache.

        Returns:
            The value associated with the key, or None if the key does not exist.
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
