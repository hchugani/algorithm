from functools import lru_cache


class Solution:

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        def compress_len(seq_len):
            if not seq_len:
                return 0
            if seq_len==1:
                return 1
            elif seq_len<10:
                return 2
            elif seq_len<100:
                return 3
            elif seq_len<1000:
                return 4
            elif seq_len<10000:
                return 5

        @lru_cache(maxsize=None)
        def min_len(ind=0, last_chr="", last_count=0, rem=k):

            if ind>=len(s):
                return compress_len(last_count)

            possible_lens = []

            if rem: # delete this one
                possible_lens.append(min_len(ind+1, last_chr, last_count, rem-1))
            if s[ind]==last_chr:# keep it, dont compress yet
                possible_lens.append(min_len(ind+1, last_chr, last_count+1, rem))
            else: # compress prev last count
                possible_lens.append(min_len(ind+1, s[ind], 1, rem)+compress_len(last_count))

            return min(possible_lens)

        return min_len()

sol = Solution()
inputs = [
    ("aaabcccd",
     2)
]

for s, k in inputs:
    print(sol.getLengthOfOptimalCompression(s,k))