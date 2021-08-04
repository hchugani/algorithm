"""
           Trie
                        root
                    /   \    \
                    t   a     b
                    |   |     |
                    h   n     y
                    |   |  \  |
                    e   s  y  e
                 /  |   |
                 i  r   w
                 |  |   |
                 r  e   e
                        |
                        r

"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEndOfWord = False

class Trie:
    """
    insert, search time complexity: O[M], M is max key  length
    Space complexity O(alphabet_size * M * N) number of keys
    """

    def __init__(self):
        self.root = self.getNode()

    def getNode(self):
        return  TrieNode()

    def _charToIndex(self, ch):
        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        return ord(ch)-ord('a')

    def insertKey(self, key):

        pCrawl = self.root
        for i in range(len(key)):
            index = self._charToIndex(key[i])
            if pCrawl.children[index] is  None:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]
        pCrawl.isEndOfWord = True

    def search(self, key)->bool:
        pCrawl =self.root
        for i in range(len(key)):
            index = self._charToIndex(key[i])
            if pCrawl.children[index] is  None:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndOfWord

if __name__ == '__main__':
    keys = ["the","a","there","anaswe","any",
            "by","their"]

    trie = Trie()
    for key in keys:
        trie.insertKey(key)

    print(trie.search("anaswe"))
