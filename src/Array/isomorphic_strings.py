

class Solution:
    """
    Given two strings s and t, determine if they are isomorphic.

    Two strings s and t are isomorphic if the characters in s can be replaced to get t.

    All occurrences of a character must be replaced with another character while preserving the
    order of characters. No two characters may map to the same character, but a character may map
     to itself.

    Example 1:

    Input: s = "egg", t = "add"
    Output: true
    Example 2:

    Input: s = "foo", t = "bar"
    Output: false

    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        """

        Time complexity : O(N)
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False

        mapper = {}
        mapper2 = {}

        for i in range(len(s)):
            if s[i] not in mapper:
                mapper[s[i]] = t[i]
            else:
                if mapper[s[i]] != t[i]:
                    return False
            if t[i] not in mapper2:
                mapper2[t[i]] = s[i]
            else:
                if mapper2[t[i]] != s[i]:
                    return False

        return True


s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("ege", "add"))