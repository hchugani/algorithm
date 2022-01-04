class Solution:
    def maxValue(self, n: str, x: int) -> str:
        """
        O(N)
        """
        ret = ""
        neg = False
        found = False
        if n and n[0]=="-":
            neg = True

        if not neg:
            i = 0
            while i < len(n):
                if x>int(n[i]):
                    ret += str(x)
                    found = True
                    break
                else:
                    ret += n[i]
                    i+=1
            while i < len(n):
                ret += n[i]
                i+=1
            if not found:
                ret +=str(x)
        else:
            ret = "-"
            i = 1
            while i < len(n):
                if  x<int(n[i]):
                    ret += str(x)
                    found = True
                    break
                else:
                    ret += n[i]
                    i+=1
            while i < len(n):
                ret += n[i]
                i+=1
            if not found:
                ret +=str(x)

        return ret

    def maxValue(self, n: str, x: int) -> str:
        x = str(x)
        is_negative = n[0] == '-'
        for index, digit in enumerate(n):
            if is_negative and x < digit or not is_negative and x > digit:
                return n[:index] + x + n[index:]
        return n + x

s = Solution()
inputs = [
    ("99",9), ("-132", 3)
]

for n, x in inputs:
    print(s.maxValue(n,x))