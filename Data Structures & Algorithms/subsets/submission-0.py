class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(comb,index):
            if index == len(nums):
                ans.append(comb[:])
                return

            comb.append(nums[index])
            backtracking(comb,index + 1)
            comb.pop()
            backtracking(comb,index + 1)
        
        backtracking([],0)
        return ans