# my solution https://leetcode.com/problems/insert-delete-getrandom-o1/

from random import choice


class RandomizedSet:

    def __init__(self):
        self.data = set()

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        try:
            self.data.remove(val)
            return True
        except:
            return False

    def getRandom(self) -> int:
        return choice(list(self.data))

# more optimized solution

import random


class RandomizedSet:

    def __init__(self):
        self.data = {}  # Map value to index in the list
        self.values = []  # List to store values for O(1) access

    def insert(self, val: int) -> bool:
        if val not in self.data:
            self.data[val] = len(self.values)  # Store index of the value
            self.values.append(val)  # Append the value to the list
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.data:
            # Swap the element with the last element to maintain O(1) removal
            index_to_remove = self.data[val]
            last_element = self.values[-1]

            # Swap last element with the element to remove
            self.values[index_to_remove] = last_element
            self.data[last_element] = index_to_remove

            # Remove the last element
            self.values.pop()
            del self.data[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.values)
