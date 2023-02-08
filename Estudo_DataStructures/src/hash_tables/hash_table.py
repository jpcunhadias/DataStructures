from typing import Optional, Tuple


class HashMap:
    """
    A class that implements a hash map data structure.

    The hash map uses a list of size 'size' as the underlying data structure, where each element
    in the list represents a "bucket" where key-value pairs with the same hash can be stored. The
    hash function is used to calculate the index of the bucket where a key-value pair should be
    stored, and the add, get, and delete methods are used to add, retrieve, and delete key-value
    pairs from the hash map, respectively.

    Attributes:
    size (int): The number of buckets in the hash map. Default value is 16.
    map (list): The underlying list data structure that represents the hash map.
    """

    def __init__(self, size: int = 16):
        self.size = size
        self.map = [None] * size

    def _get_index(self, key: int) -> int:
        """
        Calculates the index of the bucket where the key-value pair should be stored.
        """
        return key % self.size

    def add(self, key: int, value: int) -> None:
        """
        Adds a key-value pair to the hash map.

        Args:
        key (int): The key of the key-value pair.
        value (int): The value of the key-value pair.
        """
        index = self._get_index(key)
        current_bucket = self.map[index]

        if current_bucket is None:
            self.map[index] = []

        self.map[index].append((key, value))

    def get(self, key: int) -> Optional[int]:
        """
        Retrieves the value associated with the given key.

        Args:
        key (int): The key of the key-value pair to retrieve.

        Returns:
        Optional[int]: The value associated with the given key, or None if the key is not found.
        """
        index = self._get_index(key)
        current_bucket = self.map[index]

        if current_bucket is None:
            return None

        for k, v in current_bucket:
            if k == key:
                return v

        return None

    def delete(self, key: int) -> None:
        """
        Deletes the key-value pair with the given key from the hash map.

        Args:
        key (int): The key of the key-value pair to delete.
        """
        index = self._get_index(key)
        current_bucket = self.map[index]

        if current_bucket is None:
            return

        for i, (k, v) in enumerate(current_bucket):
            if k == key:
                current_bucket.pop(i)
                break

    def print(self):
        print('---PHONEBOOK----')
        for item in self.map:
            if item is not None:
                print(str(item))
