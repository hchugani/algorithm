from typing import List


class Solution:
    """
    Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left-justified and no extra space is inserted between words.

    Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.


    Example 1:

    Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    Output:
    [
       "This    is    an",
       "example  of text",
       "justification.  "
    ]
    """
    def fullJustify(self, wordList: List[str], max_len: int) -> List[str]:
        """
        Timecomplexity  and space : O(lines * max_len)
        :param wordList:
        :param max_len:
        :return:
        """
        lineArr = []
        currline = []
        cur_len = 0
        i = 0
        while i<len(wordList):
            word = wordList[i]
            if len(word)+cur_len<=max_len:
                if len(word)+cur_len+1 <= max_len:
                    currline.append(word+" ")
                    cur_len += len(word)+1
                else:
                    currline.append(word)
                    cur_len += len(word)
                i+=1
            else:
                space = max_len - cur_len
                index = 0
                if currline[-1][-1]==" ":
                    currline[-1] = currline[-1][:-1]
                    space+=1
                while space>0:
                    currline[index] += " "
                    space-=1
                    index +=1
                    index %= ((len(currline)-1) or 1)
                joinedstr = "".join(currline)
                lineArr.append(joinedstr)
                currline = []
                cur_len = 0
        if currline:
            space = max_len - cur_len
            currline[-1] += (" "*space)
            joinedstr = "".join(currline)
            lineArr.append(joinedstr)
        return lineArr


s = Solution()
word_list = ["This", "is", "an", "example", "of", "text", "justification."]
print(s.fullJustify(word_list,16))