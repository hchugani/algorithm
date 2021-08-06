
class SubstrConcatAllWords:
    """
    Time complexity : O(N*W)
    Space Complexity : O(N)
    """
    def getMatchngIndexs(self, s : str, words : [])-> []:
        result = []
        step = len(words[0])
        mapper = {}
        for word in words:
            if word not in mapper.keys(): mapper[word]=0
            mapper[word]+=1

        r = 0
        while r < len(s)-len(words)*step+1:
            freq = {}
            temp =  s[r:r+step*len(words)]
            i = 0
            while i < len(temp) - step + 1:
                if temp[i:i+step] not in freq.keys(): freq[temp[i:i+step]]=0
                freq[temp[i:i+step]] +=1
                i+=step
            if self.dictComp(mapper, freq):
                result.append(r)
            r+=1
        return result

    def dictComp(self, s1, s2)->bool:
        for key, val in s1.items():
            if key not in s2.keys():
                return False
            elif val != s2[key]:
                return False
        return True

if __name__ == "__main__":
    ss = SubstrConcatAllWords()
    s = "barfoothefoobarman"
    words = ["foo","bar"]
    print(ss.getMatchngIndexs(s, words=words))
