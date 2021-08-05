import sys

class TripleSubsequence:
    def increasingTriplet(self, nums: []) -> bool:
        first = sys.maxsize
        second = sys.maxsize

        for n in nums:
            if n<=first:
                first = n
            elif n<=second:
                second = n
            else:
                return True

        return False

if __name__ == "__main__":
    nums = [4, 5, 1, 2, 6]
    t = TripleSubsequence()
    print(t.increasingTriplet(nums))
