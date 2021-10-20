"""
1804. Implement Trie II (Prefix Tree)
Medium

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and
retrieve keys in a dataset of strings. There are various applications of this data structure, such as
autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
int countWordsEqualTo(String word) Returns the number of instances of the string word in the trie.
int countWordsStartingWith(String prefix) Returns the number of strings in the trie that have the
string prefix as a prefix.
void erase(String word) Erases the string word from the trie.


Example 1:

Input
["Trie", "insert", "insert", "countWordsEqualTo", "countWordsStartingWith", "erase", "countWordsEqualTo",
"countWordsStartingWith", "erase", "countWordsStartingWith"]
[[], ["apple"], ["apple"], ["apple"], ["app"], ["apple"], ["apple"], ["app"], ["apple"], ["app"]]
Output
[null, null, null, 2, 2, null, 1, 1, null, 0]

Explanation
Trie trie = new Trie();
trie.insert("apple");               // Inserts "apple".
trie.insert("apple");               // Inserts another "apple".
trie.countWordsEqualTo("apple");    // There are two instances of "apple" so return 2.
trie.countWordsStartingWith("app"); // "app" is a prefix of "apple" so return 2.
trie.erase("apple");                // Erases one "apple".
trie.countWordsEqualTo("apple");    // Now there is only one instance of "apple" so return 1.
trie.countWordsStartingWith("app"); // return 1
trie.erase("apple");                // Erases "apple". Now the trie is empty.
trie.countWordsStartingWith("app"); // return 0

"""

class Node:
    def __init__(self):
        self.children = [None]*26
        self.isEndofWord = False
        self.count = 0 # no of occurencs
        self.shared = 0

class Trie:
    """
    insert, search time complexity: O[M], M is max key  length
    Space complexity O(alphabet_size * M * N) number of keys

    """

    def __init__(self):
        self.root = self.get_node()

    def get_node(self):
        return Node()

    def _charToIndex(self,c):
        return ord(c)-ord("a")

    def insert(self, word: str) -> None:
        crawl = self.root
        for s in word:
            index = self._charToIndex(s)
            if crawl.children[index] is None:
                crawl.children[index] = self.get_node()
            crawl.children[index].shared +=1
            crawl = crawl.children[index]
        crawl.isEndofWord = True
        crawl.count +=1


    def countWordsEqualTo(self, word: str) -> int:
        crawl = self.root
        for s in word:
            index = self._charToIndex(s)
            if crawl.children[index] is None:
                return 0
            crawl = crawl.children[index]
        return crawl.count


    def countWordsStartingWith(self, prefix: str) -> int:
        crawl = self.root
        for s in prefix:
            index = self._charToIndex(s)
            if crawl.children[index] is None:
                return 0
            crawl = crawl.children[index]
        return crawl.shared

    def search(self, key)->bool:
        pCrawl =self.root
        for s in key:
            index = self._charToIndex(s)
            if pCrawl.children[index] is  None:
                return False
            pCrawl = pCrawl.children[index]
        return pCrawl.isEndofWord

    def erase(self, word: str) -> None:
        if not self.search(word):
            return None

        crawl = self.root
        for s in word:
            index = self._charToIndex(s)
            crawl.children[index].shared-=1
            crawl = crawl.children[index]

        crawl.count-=1


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert("apple")
obj.insert("apple")
print(obj.countWordsEqualTo("apple"))
obj.insert("app")
print(obj.countWordsStartingWith("app"))
obj.erase("apple")
print(obj.countWordsEqualTo("apple"))