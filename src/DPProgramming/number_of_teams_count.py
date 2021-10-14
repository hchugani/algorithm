"""
There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])
where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).



Example 1:

Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

"""


from typing import List
class Solution:
    def numTeams(self, rating: List[int]) -> int:

        """
        O(n*n*n)
        """
        """
        for i in range(len(rating_with_pos)):
            for j in range(i+1, len(rating_with_pos) ):
                for k in range(j+1, len(rating_with_pos)):
                    if rating_with_pos[i][1] < rating_with_pos[j][1] < rating_with_pos[k][1]:
                        self.result+=1
                    
                    if rating_with_pos[i][1] > rating_with_pos[j][1] > rating_with_pos[k][1]:
                        self.result+=1
                        
        
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j]>rating[i]:
                    great_dict[i].append(j)
                elif rating[j]<rating[i]:
                    less_dict[i].append(j)
                    
        for i in range(len(rating)):
            for index in great_dict[i]:
                self.result += len(great_dict[index])
            
            for index in less_dict[i]:
                self.result += len(less_dict[index])
                
        """
        """
        O(n*n) time complexity
        O(n) space complexity
        """
        answer = 0
        g = [0]*len(rating)
        s = [0]*len(rating)

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j]>rating[i]:
                    g[i]+=1
                elif rating[j]<rating[i]:
                    s[i]+=1

        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[j]>rating[i]:
                    answer+=g[j]
                elif rating[j]<rating[i]:
                    answer+=s[j]

        return answer


s = Solution()
inputs = [
    [2,5,3,4,1],
    [2,1,3],
    [1,2,3,4]
]

for input in inputs:
    print(s.numTeams(input))

