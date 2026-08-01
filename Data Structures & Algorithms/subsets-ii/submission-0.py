class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        def backtracking(comb,start):
            ans.append(comb[:])
            if start == len(nums):
                return
            for i in range(start,len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                comb.append(nums[i])
                backtracking(comb,i + 1)
                comb.pop()
        backtracking([],0)
        return ans