class Solution:
    def hammingWeight(self, n: int) -> int:
        # % | ^ ~
        mask = 1
        cnt = 0
        for i in range(32):
            if n & (mask << i) != 0:
                cnt += 1
        return cnt