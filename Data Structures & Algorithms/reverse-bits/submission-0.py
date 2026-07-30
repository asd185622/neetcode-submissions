class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 1
        ans = 0
        for i in range(32):
           b = (n >> i) & 1
           ans |= (b << (31 - i))

        return ans