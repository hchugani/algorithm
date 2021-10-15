

class Solution:
    def numSplits(self, s: str) -> int:
        """
        O(n) time complexity, O(1) space complexity

        :param s:
        :return:
        """
        result = 0

        counter_map = {}
        for c in s:
            if c not in counter_map:
                counter_map[c] = 0
            counter_map[c] +=1

        remove_map = {}

        for c in s:
            if c in counter_map:
                counter_map[c]-=1
                if counter_map[c] == 0:
                    del counter_map[c]

            if c not in remove_map:
                remove_map[c] = 0
            remove_map[c] +=1

            if len(remove_map.keys()) == len(counter_map.keys()):
                result +=1

        """
        for i in range(1, len(s)):
            left_map = set()
            right_map = set()
            
            for j in range(0, i):
                left_map.add(s[j])
            
            for j in range(i, len(s)):
                right_map.add(s[j])
                
            if len(left_map)==len(right_map):
                result+=1
        """

        return result


s = Solution()
inputs = [
    "aacaba",
    "aaaaa",
    "acbadbaada"
]

for input in inputs:
    print(s.numSplits(input))