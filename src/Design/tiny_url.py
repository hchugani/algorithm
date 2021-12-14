import random
import sys


class Codec:

    def __init__(self):
        self.map = {}
        self.chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = self.getRand()

    def getRand(self):
        new_key = ""
        for _ in range(6):
            new_key += self.chars[random.randint(0,61)]
        return new_key

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while(self.key in self.map.keys()):
            self.key = self.getRand()

        self.map[self.key] = longUrl
        return "tinyurl.com/"+self.key




    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        key = shortUrl.replace("tinyurl.com/", "")
        return self.map[key]

# Your Codec object will be instantiated and called as such:
codec = Codec()
long_url = "www.longurl.com/"
for i in range(sys.maxsize):
    url = long_url+str(i)
    print(codec.decode(codec.encode(url)))