from typing import List
import random

class Solution:
    """
    Problem
    You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

    We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex() should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

    More formally, the probability of picking index i is w[i] / sum(w).



    Example 1:

    Input
    ["Solution","pickIndex"]
    [[[1]],[]]
    Output
    [null,0]

    Explanation
    Solution solution = new Solution([1]);
    solution.pickIndex(); // return 0. Since there is only one single element on the array the only option is to return the first element.

    """

    """
    Solution:
    This is actually a very practical problem which appears often in the scenario where we need to do sampling over a set of data.

    Nowadays, people talk a lot about machine learning algorithms. As many would reckon, one of the basic operations involved in training a machine learning algorithm (e.g. Decision Tree) is to sample a batch of data and feed them into the model, rather than taking the entire data set. There are several rationales behind doing sampling over data, which we will not cover in detail, since it is not the focus of this article.
    
    If one is interested, one can refer to our Explore card of Machine Learning 101 which gives an overview on the fundamental concepts of machine learning, as well as the Explore card of Decision Tree which explains in detail on how to construct a decision tree algorithm.
    
    Now, given the above background, hopefully one is convinced that this is an interesting problem, and it is definitely worth solving.
    
    Intuition
    
    Given a list of positive values, we are asked to randomly pick up a value based on the weight of each value. To put it simple, the task is to do sampling with weight.
    
    Let us look at a simple example. Given an input list of values [1, 9], when we pick up a number out of it, the chance is that 9 times out of 10 we should pick the number 9 as the answer.
    
    In other words, the probability that a number got picked is proportional to the value of the number, with regards to the total sum of all numbers.
    
    To understand the problem better, let us imagine that there is a line in the space, we then project each number into the line according to its value, i.e. a large number would occupy a broader range on the line compared to a small number. For example, the range for the number 9 should be exactly nine times as the range for the number 1.
    
    throw a ball
    
    Now, let us throw a ball randomly onto the line, then it is safe to say there is a good chance that the ball will fall into the range occupied by the number 9. In fact, if we repeat this experiment for a large number of times, then statistically speaking, 9 out of 10 times the ball will fall into the range for the number 9.
    
    Voila. That is the intuition behind this problem.
    
    Simulation
    
    So to solve the problem, we can simply simulate the aforementioned experiment with a computer program.
    
    First of all, let us construct the line in the experiment by chaining up all values together.
    
    Let us denote a list of numbers as [w_1, w_2, w_3, ..., w_n][w 
    1
    ​
     ,w 
    2
    ​
     ,w 
    3
    ​
     ,...,w 
    n
    ​
     ]. Starting from the beginning of the line, we then can represent the offsets for each range KK as (\sum_{1}^{K}{w_i}, \sum_{1}^{K+1}{w_i})(∑ 
    1
    K
    ​
     w 
    i
    ​
     ,∑ 
    1
    K+1
    ​
     w 
    i
    ​
     ), as shown in the following graph:
    
    prefix sum formula
    
    As many of you might recognize now, the offsets of the ranges are actually the prefix sums from a sequence of numbers. For each number in a sequence, its corresponding prefix sum, also known as cumulative sum, is the sum of all previous numbers in the sequence plus the number itself.
    
    As an observation from the definition of prefix sums, one can see that the list of prefix sums would be strictly monotonically increasing, if all numbers are positive.
    
    To throw a ball on the line is to find an offset to place the ball. Let us call this offset target.
    
    Once we randomly generate the target offset, the task is now boiled down to finding the range that this target falls into.
    
    Let us rephrase the problem now, given a list of offsets (i.e. prefix sums) and a target offset, our task is to fit the target offset into the list so that the ascending order is maintained.
    
    
    
    Approach 1: Prefix Sums with Linear Search
    Intuition
    
    If one comes across this problem during an interview, one can consider the problem almost resolved, once one reduces the original problem down to the problem of inserting an element into a sorted list.
    
    Concerning the above problem, arguably the most intuitive solution would be linear search. Many of you might have already thought one step ahead, by noticing that the input list is sorted, which is a sign to apply a more advanced search algorithm called binary search.
    
    Let us do one thing at one time. In this approach, we will first focus on the linear search algorithm so that we could work out other implementation details. In the next approach, we will then improve upon this approach with a binary search algorithm.
    
    So far, there is one little detail that we haven't discussed, which is how to randomly generate a target offset for the ball. By "randomly", we should ensure that each point on the line has an equal opportunity to be the target offset for the ball.
    
    In most of the programming languages, we have some random() function that generates a random value between 0 and 1. We can scale up this randomly-generated value to the entire range of the line, by multiplying it with the size of the range. At the end, we could use this scaled random value as our target offset.
    
    As an alternative solution, sometimes one might find a randomInteger(range) function that could generate a random integer from a given range. One could then directly use the output of this function as our target offset.
    
    Here, we adopt the random() function, since it could also work for the case where the weights are float values.
    
    Algorithm
    
    We now should have all the elements at hand for the implementation.
    
    First of all, before picking an index, we should first set up the playground, by generating a list of prefix sums from a given list of numbers. The best place to do so would be in the constructor of the class, so that we don't have to generate it again and again at the invocation of pickIndex() function.
    
    In the constructor, we should also keep the total sum of the input numbers, so that later we could use this total sum to scale up the random number.
    For the pickIndex() function, here are the steps that we should perform.
    
    Firstly, we generate a random number between 0 and 1. We then scale up this number, which will serve as our target offset.
    
    We then scan through the prefix sums that we generated before by linear search, to find the first prefix sum that is larger than our target offset.
    
    And the index of this prefix sum would be exactly the right place that the target should fall into. We return the index as the result of pickIndex() function.
    """

    def __init__(self, w: List[int]):

        # prefix sum to build the wts along the line
        self.prefix_sums = []


        prefix_sum = 0
        for wt in w:
            prefix_sum += wt
            self.prefix_sums.append(prefix_sum)
        self.total_sum = prefix_sum


    def pickIndex(self) -> int:
        """
        time complexity : O(N) with linear search and O(NlogN) with binary search
        space complexity is O(N)
        *******
        https://leetcode.com/problems/random-pick-with-weight/solution/


        :return:
        """
        # random.random() pics value between 0 and 1
        # which is multplied by total_sun
        # then we look for bucket which it falls
        target = self.total_sum * random.random()

        # Linear search
        # for index, prefix_sum in enumerate(self.prefix_sums):
        #     if target < prefix_sum:
        #         return index

        # Binary Search
        l, r = 0, len(self.prefix_sums)

        while l<r:
            pivot = l + (r-l)//2
            if target < self.prefix_sums[pivot]:
                if pivot==0 or (pivot-1>=0 and target>self.prefix_sums[pivot-1]):
                    return pivot
                else:
                    r = pivot
            elif target>self.prefix_sums[pivot]:
                l = pivot
            else:
                return pivot