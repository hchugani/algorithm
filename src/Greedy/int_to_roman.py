class Solution:
    def intToRoman(self, num: int) -> str:
        """
        O(1) both
        :param num:
        :return:
        """
        divs = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5,4, 1]
        roman = ["M", "CM", "D", "CD", "C", "XC", "L","XL" ,"X", "IX", "V", "IV", "I"]

        s = ""
        val = num
        for i in range(len(divs)):
            if val==0:
                break
            x = val//divs[i]
            s += x * roman[i]
            val = val%divs[i]

        return s

s = Solution()
for i in [1998, 3, 5600]:
    print(s.intToRoman(i))