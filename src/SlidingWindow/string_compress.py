"""

443. String Compression
Medium

Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array
 chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
"""

from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        O(N): Time
        O(1): space
        """
        res = 0
        r = l = 0
        while l < len(chars):
            while r < len(chars) and chars[l]==chars[r]:
                r+=1
            temp = chars[l]+ str(r-l) if r-l>1 else chars[l]
            for c in temp:
                chars[res] = c
                res+=1
            l = r

        return res

s = Solution()
inputs = [
    ["a","a","b","b","c","c","c"],
    ["a","a","a","a","a","a","a","a","a","a","a","a","a","b","b","c","c","c"]
]

for arr in inputs:
    new_len = s.compress(arr)
    print(arr[:new_len])