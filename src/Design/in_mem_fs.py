from collections import defaultdict
from typing import List

"""
588. Design In-Memory File System
Hard

Design a data structure that simulates an in-memory file system.

Implement the FileSystem class:

FileSystem() Initializes the object of the system.
List<String> ls(String path)
If path is a file path, returns a list that only contains this file's name.
If path is a directory path, returns the list of file and directory names in this directory.
The answer should in lexicographic order.
void mkdir(String path) Makes a new directory according to the given path. The given directory path does
 not exist. If the middle directories in the path do not exist, you should create them as well.
void addContentToFile(String filePath, String content)
If filePath does not exist, creates that file containing given content.
If filePath already exists, appends the given content to original content.
String readContentFromFile(String filePath) Returns the content in the file at filePath.
"""

class TrieNode:

    def __init__(self):
        self.mapper = defaultdict(TrieNode)
        self.isFile = False
        self.contents = ""

class FileSystem:

    def __init__(self):
        self.top = TrieNode()


    def ls(self, path: str) -> List[str]:
        path_names = path.split("/")
        node = self.top
        for p in path_names:
            if not p:
                continue
            node = node.mapper[p]
        if node.isFile:
            return [p]
        ans = [ key for key in node.mapper.keys()]
        if not ans:
            return ans
        ans.sort()
        return ans



    def mkdir(self, path: str) -> None:
        path_names = path.split("/")
        node = self.top
        for p in path_names:
            if not p:
                continue
            node = node.mapper[p]


    def addContentToFile(self, filePath: str, content: str) -> None:
        path_names = filePath.split("/")
        node = self.top
        for p in path_names:
            if not p:
                continue
            node = node.mapper[p]
        node.contents += content
        node.isFile =True



    def readContentFromFile(self, filePath: str) -> str:
        path_names = filePath.split("/")
        node = self.top
        for p in path_names:
            if not p:
                continue
            node = node.mapper[p]
        if node.isFile:
            return node.contents



# Your FileSystem object will be instantiated and called as such:
obj = FileSystem()
param_1 = obj.ls("/")
obj.mkdir("/a/b/nm")
obj.addContentToFile("/a/b/nm/d","content")
print(obj.readContentFromFile("/a/b/nm/d"))