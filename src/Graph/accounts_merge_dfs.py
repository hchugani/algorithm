from collections import defaultdict
from typing import List

"""
721. Accounts Merge
Medium

Given a list of accounts where each element accounts[i] is a list of strings, where the first element 
accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there
 is some common email to both accounts. Note that even if two accounts have the same name, they may belong 
 to different people as people could have the same name. A person can have any number of accounts initially,
  but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account
 is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be 
 returned in any order.

"""

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Time complexity: O(NKlogNK)

        In the worst case, all the emails will end up belonging to a single person. The total number of emails will be N∗K, and we need to sort these emails. DFS traversal will take NK operations as no email will be traversed more than once.

        Space complexity: O(NK)

        """


        """
        Using strongly connected components
        
        Here, we will represent emails as nodes, and an edge will signify that two emails are connected and hence belong to the same person. This means that any two emails that are connected by a path of edges must also belong to the same person. Initially, we are given NN accounts, where each account's emails make up a connected component.

Our first step should be to ensure that for each account, all of its nodes are connected. Suppose an account has KK emails, and we want to connect these emails. Since all emails in an account are connected, we can add an edge between every pair of emails. This will create a complete subgraph and require adding K \choose 2( 
2
K
​
 ) edges. However, do we really need that many edges to keep track of which emails belong to the same account? No, as long as two emails are connected by a path of edges, we know they belong to the same account. So instead of creating a complete subgraph for each account, we can create an acyclic graph using only K - 1K−1 edges. Recall that K - 1K−1 is the minimum number of edges required to connect KK nodes. In this approach, we will connect emails in an account in a star manner with the first email as the internal node of the star and all other emails as the leaves (as shown below).
        
        
        """
        email_map = defaultdict(list)

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                email_map[accounts[i][1]].append((accounts[i][j], i))
                email_map[accounts[i][j]].append((accounts[i][1], i))

        visited = set()

        def dfs(key,merge):
            visited.add(key)

            for email,i in email_map[key]:
                merge.add(i)
                if email not in visited:
                    dfs(email,merge)

        result = []
        for key in email_map.keys():
            if key not in visited:
                merge = set()
                dfs(key, merge)
                temp = set()
                key = ""
                for i in merge:
                    key = accounts[i][0]
                    for j in range(1,len(accounts[i])):
                        temp.add(accounts[i][j])
                temp = sorted(list(temp))
                if key:
                    result.append([key]+temp)

        return result



s= Solution()

inputs = [
    [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]],
    [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
]

for inp in inputs:
    print(s.accountsMerge(inp))