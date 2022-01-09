"""
1152. Analyze User Website Visit Pattern
Medium


You are given two string arrays username and website and an integer array timestamp. All the given arrays are of the
same length and the tuple [username[i], website[i], timestamp[i]] indicates that the user username[i] visited the website website[i] at time timestamp[i].

A pattern is a list of three websites (not necessarily distinct).

For example, ["home", "away", "love"], ["leetcode", "love", "leetcode"], and ["luffy", "luffy", "luffy"] are all
 patterns.
The score of a pattern is the number of users that visited all the websites in the pattern in the same order they
appeared in the pattern.

For example, if the pattern is ["home", "away", "love"], the score is the number of users x such that x visited "home"
 then visited "away" and visited "love" after that.
Similarly, if the pattern is ["leetcode", "love", "leetcode"], the score is the number of users x such that x visited
"leetcode" then visited "love" and visited "leetcode" one more time after that.
Also, if the pattern is ["luffy", "luffy", "luffy"], the score is the number of users x such that x visited "luffy" t
hree different times at different timestamps.
Return the pattern with the largest score. If there is more than one pattern with the same largest score, return
 the lexicographically smallest such pattern.
"""

"""
Pretty much followed the hint from the description

Get (time, website) records per user
Find & count all 3-sequences for each user
Find the one appeared most
Things need to be aware of:
sequence not continuous sequence, meaning websites in 3-sequence doesn't have to be next to each other
Even if a 3-sequence appears more than one time for some user, it should only counted as once, since the 3-sequence
is defined at a user/per-person level. (quote: Find the 3-sequence visited by the largest number of users..
It's NOT asking us to "Find the 3-sequence visited most frequently")
"""
from collections import defaultdict
from typing import List

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:

        users_to_website = defaultdict(list)
        counter = defaultdict(int)

        logs = []
        for u, t, w  in zip(username,timestamp, website):
            logs.append((u, t, w))

        logs.sort(key= lambda x : x[1])


        for log in logs:
            user = log[0]
            time = log[1]
            web = log[2]
            users_to_website[user].append((time,web))

        for user in users_to_website.keys():
            records = users_to_website[user]
            visited = set()
            for i in range(len(records)):
                for j in range(i+1, len(records)):
                    for k in range(j+1,len(records)):
                        if (records[i][1], records[j][1], records[k][1]) not in visited:
                            counter[(records[i][1], records[j][1], records[k][1])]+=1
                            visited.add((records[i][1], records[j][1], records[k][1]))

        # s
        ans = sorted(counter.items(),key=lambda x : (-x[1], x[0]),reverse=True)
        return ans[-1][0]

s = Solution()
inputs = [
    (["joe","joe","joe","james","james","james","james","mary","mary","mary"],
    [1,2,3,4,5,6,7,8,9,10],
    ["home","about","career","home","cart","maps","home","home","about","career"]),
    (["him","mxcmo","jejuvvtye","wphmqzn","uwlblbrkqv","flntc","esdtyvfs","nig","jejuvvtye",
      "nig","mxcmo","flntc","nig","jejuvvtye","odmspeq","jiufvjy","esdtyvfs","mfieoxff",
      "nig","flntc","mxcmo","qxbrmo"],
    [113355592,304993712,80831183,751306572,34485202,414560488,667775008,951168362,794457022,
     813255204,922111713,127547164,906590066,685654550,430221607,699844334,358754380,301537469,
     561750506,612256123,396990840,60109482],
    ["k","o","o","nxpvmh","dssdnkv","kiuorlwdcw","twwginujc","evenodb","qqlw","mhpzoaiw",
     "jukowcnnaz","m","ep","qn","wxeffbcy","ggwzd","tawp","gxm","pop","xipfkhac","weiujzjcy","x"])
]

for u, t, w in inputs:
    print(s.mostVisitedPattern(u,t,w))


