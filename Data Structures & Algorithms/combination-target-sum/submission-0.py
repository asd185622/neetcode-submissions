class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def backtracking(comb,currSum,start):
            if currSum > target:
                return
            if currSum == target:
                res.append(comb[:])
            
            for i in range(start,len(nums)):
                comb.append(nums[i])
                currSum += nums[i]
                backtracking(comb,currSum,i)
                comb.pop()
                currSum -= nums[i]
        
        backtracking([],0,0)
        return res