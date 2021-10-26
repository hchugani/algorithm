"""
1647. Minimum Deletions to Make Character Frequencies Unique
Medium

A string s is called good if there are no two different characters in s that have the same frequency.

Given a string s, return the minimum number of characters you need to delete to make s good.

The frequency of a character in a string is the number of times it appears in the string. For example,
 in the string "aab", the frequency of 'a' is 2, while the frequency of 'b' is 1.



Example 1:

Input: s = "aab"
Output: 0
Explanation: s is already good.
Example 2:

Input: s = "aaabbbcc"
Output: 2
Explanation: You can delete two 'b's resulting in the good string "aaabcc".
Another way it to delete one 'b' and one 'c' resulting in the good string "aaabbc".
Example 3:

Input: s = "ceabaacb"
Output: 2
Explanation: You can delete both 'c's resulting in the good string "eabaab".
Note that we only care about characters that are still in the string at the end (i.e. frequency of 0
is ignored).

"""
class Solution:
    def minDeletions(self, s: str) -> int:
        """
        O(n) both
        """
        counter = {}

        for c in s:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1

        if len(counter.keys())<2:
            return 0

        # sorting O(1)
        sorted_keys = sorted(counter.keys(), key= lambda x: counter[x], reverse=True)

        num = 0
        for i in range(1, len(sorted_keys)):
            while 0<counter[sorted_keys[i]] >= counter[sorted_keys[i-1]]:
                counter[sorted_keys[i]]-=1
                num+=1

        return num

s= Solution()
inputs = [
    "aab",
    "aaabbbcc",
    "ceabaacb",
    "aaa",
    "abcabc",
    "bbcebab",
]

for inp in inputs:
    print(s.minDeletions(inp))


