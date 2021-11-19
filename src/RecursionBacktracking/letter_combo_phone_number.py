"""
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the
number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not
map to any letters.

"""
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        O(4^N) : time
        O(N) : space
        """
        num_map = {}

        num_map[2] = "abc"
        num_map[3] = "def"
        num_map[4] = "ghi"
        num_map[5] = "jkl"
        num_map[6] = "mno"
        num_map[7] = "pqrs"
        num_map[8] = "tuv"
        num_map[9] = "wxyz"

        result = []

        def backtrack(i, temp = []):
            if temp and len(temp) == len(digits):
                result.append("".join(list(temp)))
                return
            if i == len(digits):
                return

            letters = num_map[int(digits[i])]

            for c in letters:
                temp.append(c)
                backtrack(i+1, temp)
                temp.pop()

        backtrack(0)

        return result


s = Solution()

for n in ["234","","2"]:
    print(s.letterCombinations(n))
