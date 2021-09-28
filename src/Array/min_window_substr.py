

class Solution:
    """
    Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

    The testcases will be generated such that the answer is unique.

    A substring is a contiguous sequence of characters within the string.



    Example 1:

    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
    Example 2:

    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.
    Example 3:

    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.


    Constraints:

    m == s.length
    n == t.length
    1 <= m, n <= 105
    s and t consist of uppercase and lowercase English letters.


    Follow up: Could you find an algorithm that runs in O(m + n) time?

    """
    def minWindow(self, s: str, t: str) -> str:
        """
        Time Complexity: O(|S| + |T|)O(∣S∣+∣T∣) where |S| and |T| represent the lengths of strings SS and TT. In the worst case we might end up visiting every element of string SS twice, once by left pointer and once by right pointer. |T|∣T∣ represents the length of string TT.

        Space Complexity: O(|S| + |T|)O(∣S∣+∣T∣). |S|∣S∣ when the window size is equal to the entire string SS. |T|∣T∣ when TT has all unique characters.

        :param s:
        :param t:
        :return:
        """
        map = {}
        freq = {}
        occur = {}
        for c in t:
            if c not in map: map[c]=0
            map[c]+=1
        mini = len(s)+1
        l = r = 0
        shortest = ""
        while r < len(s):
            if s[r] not in freq: freq[s[r]]=0
            freq[s[r]] +=1
            while(self.matches(freq,map)):
                if mini >(r-l+1):
                    shortest = s[l:r+1]
                    mini = r-l+1
                freq[s[l]]-=1
                l+=1
            r+=1
        return shortest


    def matches(self, s1 : dict, s2: dict)->bool:
        for key in s2.keys():
            if key not in s1:
                return False
            elif s1[key]<s2[key]:
                return False
        return True

sol = Solution()
inputs = [ ("ADOBECODEBANC","ABC")
]
for s, t in inputs:
    print(sol.minWindow(s,t))