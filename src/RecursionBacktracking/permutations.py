from typing import List

class Solution:
    """
   Approach 1: Backtracking
   Backtracking is an algorithm for finding all solutions by exploring all potential candidates. If the solution candidate turns to be not a solution (or at least not the last one), backtracking algorithm discards it by making some changes on the previous step, i.e. backtracks and then try again.

   Here is a backtrack function which takes the index of the first integer to consider as an argument backtrack(first).

   If the first integer to consider has index n that means that the current permutation is done.
   Iterate over the integers from index first to index n - 1.
   Place i-th integer first in the permutation, i.e. swap(nums[first], nums[i]).
   Proceed to create all permutations which starts from i-th integer : backtrack(first + 1).
   Now backtrack, i.e. swap(nums[first], nums[i]) back.

   """
    """
    Given an array nums of distinct integers, return all the possible permutations. You can
    return the answer in any order.

    Example 1:

    Input: nums = [1,2,3]
    Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

    Time complexity : \mathcal{O}(\sum_{k = 1}^{N}{P(N, k)})O(∑ k=1
    N
    ​
     P(N,k)) where P(N, k) = \frac{N!}{(N - k)!} = N (N - 1) ... (N - k + 1)P(N,k)=
    (N−k)!
    N!
    ​
     =N(N−1)...(N−k+1

     Space complexity: O(N!)

    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        N = len(nums)
        def backtrack(start=0):
            if start==N:
                # this will make a deep copy
                result.append(nums[:])

            for i in range(start, N):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1)
                nums[start], nums[i] = nums[i], nums[start]

        backtrack()
        return result


if __name__ == "__main__":
    sol = Solution()
    nums = [1, 2, 3]
    print(sol.permute(nums))