class Solution:
    def isNumber(self, s: str) -> bool:
        # case 1 : digits
        #  checkfor signs : it can be at the very begging or after exponent
        # . just one and it has be before e not after e , it should be just once
        # e should be comer after a digit and just once
        # last digit should be number

        seen_digit = False
        seen_dot = False
        seen_exponent = False

        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+","-"]:
                if i>0  and s[i-1] not in ["e", "E"]:
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        # last should be a digit
        return seen_digit

s = Solution()
print(s.isNumber("G37"))
print(s.isNumber("+1e7"))
