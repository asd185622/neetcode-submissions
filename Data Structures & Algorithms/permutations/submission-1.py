class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ans = []

        # def backtracking(perm):
        #     if not nums:
        #         ans.append(perm[:])
        #         return
            
        #     for i in range(len(nums)):
        #         tmp = nums.pop(i)
        #         perm.append(tmp)
        #         backtracking(perm)
        #         perm.pop()
        #         nums.insert(i,tmp)

        # backtracking([])
        # return ans

        res = []

        def backtacking(comb,valSet):
            if len(comb) == len(nums):
                res.append(comb[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in valSet:
                    continue
                comb.append(nums[i])
                valSet.add(nums[i])
                backtacking(comb,valSet)
                comb.pop()
                valSet.discard(nums[i])
        backtacking([],set())
        return res