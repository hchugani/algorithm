"""
249. Group Shifted Strings
Medium

1202

220

Add to List

Share
We can shift a string by shifting each of its letters to its successive letter.

For example, "abc" can be shifted to be "bcd".
We can keep shifting the string to form a sequence.

For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may
return the answer in any order.



Example 1:

Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
Example 2:

Input: strings = ["a"]
Output: [["a"]]
"""
from typing import List
from collections import defaultdict


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        """
        O(NK): Time
        O(N) : Space
        :param strings:
        :return:
        """

        # compute hash so that it is ame for shifts
        def hashing(s:str)->int:
            key = ""
            for a, b in zip(s, s[1:]):
                key+=chr((ord(b)-ord(a))%26+ord('a'))

            return key

        groups = defaultdict(list)

        for s in strings:
            hash_key = hashing(s)
            groups[hash_key].append(s)

        return groups.values()