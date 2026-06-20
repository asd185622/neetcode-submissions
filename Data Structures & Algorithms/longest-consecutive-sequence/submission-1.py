class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        digit = set(nums)
        search = {}    
        ans = 0
        for index,num in enumerate(nums):
            if num - 1 not in digit:
                search[num] = index

        for starter in search:
            length = 1
            while starter + 1 in digit:
                starter += 1
                length += 1
            ans = max(ans,length)
        
        return ans