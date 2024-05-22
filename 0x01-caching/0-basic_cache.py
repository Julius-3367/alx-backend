Python
#!/usr/bin/python3
""" BasicCache module """

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache inherits from BaseCaching and implements a simple cache """

    def __init__(self):
        """ Initialize the cache """
        super().__init__()  # Call parent class initializer

    def put(self, key, item):
        """ Add an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item from the cache by key """
        return self.cache_data.get(key)
