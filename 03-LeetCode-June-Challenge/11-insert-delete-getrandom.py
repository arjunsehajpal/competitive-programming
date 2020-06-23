import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._nums = []
        self._dict = {}
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self._dict:
            return False
        
        self._nums.append(val)
        self._dict[val] = len(self._nums) - 1
        return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self._dict:
            return False
        
        idx = self._dict[val]
        self._nums[idx] = self._nums[-1]
        self._dict[self._nums[idx]] = idx
        self._nums.pop()
        self._dict.pop(val)
        return True
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self._nums[random.randint(0, len(self._nums) - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()