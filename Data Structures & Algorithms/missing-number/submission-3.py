class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        maxVal = max(nums)
        ans = 0

        for i in range(1,maxVal + 1):
            ans ^= i

        for num in nums:
            ans ^= num
        
        if ans == 0 and 0 in nums:
            return len(nums)
        else:
            return ans