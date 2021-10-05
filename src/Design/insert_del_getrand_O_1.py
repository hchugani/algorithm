import random


class RandomizedSet:

    """
            Map     List
    insert  O(1)    O(1)
    remove  O(1)    O(n) to find elemnt
    random  O(n)    O(1)

    So we can have a combination
    Map which holds elment to index
    array holds elemnt
    """

    def __init__(self):
        self.ele_arry = []
        self.ele_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.ele_to_index:
            return False
        else:
            self.ele_arry.append(val)
            self.ele_to_index[val] = len(self.ele_arry)-1
            return True

    def remove(self, val: int) -> bool:
        """
        relpace the index to delete with the last element in the array
        pop the last element
        """
        if val in self.ele_to_index:
            index = self.ele_to_index[val]
            # relpace the index to delete with the last element in the array
            self.ele_arry[index] = self.ele_arry[-1]
            self.ele_to_index[self.ele_arry[index]] = index
            # pop last one
            self.ele_arry.pop()
            del self.ele_to_index[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        index = random.randint(0, len(self.ele_arry)-1)
        return self.ele_arry[index]

#Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
param_1 = obj.insert(1)
param_1 = obj.insert(2)
param_1 = obj.insert(3)
param_2 = obj.remove(2)
print(obj.getRandom())
print(obj.getRandom())