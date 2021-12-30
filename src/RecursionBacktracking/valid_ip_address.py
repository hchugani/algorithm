"""
93. Restore IP Addresses
Medium


A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255
(inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and
"192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting
dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses
in any order
"""

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        time complexity:
        255+255+255+255 - 99 -99-99-99
        :param s:
        :return:
        """
        result = []

        def backtrack(s, temp=[]):
            if len(s)==0:
                return
            if len(temp)==3:
                if len(s)>1 and s[0]=="0":
                    return
                if 0<=int(s)<=255:
                    temp.append(s)
                    result.append(list(temp))
                    temp.pop()
                return

            for i in range(len(s)):
                temp_s = s[:i+1]
                if len(temp_s)>1 and temp_s[0]=="0":
                    continue
                if 0<=int(temp_s)<=255:
                    temp.append(temp_s)
                    backtrack(s[i+1:], temp)
                    temp.pop()

        backtrack(s)
        return [".".join(arr) for arr in result]

s = Solution()
inputs = [
    "25525511135", "0000", "101023"
]
for s in inputs:
    print()