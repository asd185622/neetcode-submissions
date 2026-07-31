class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtracking(perm):
            if not nums:
                ans.append(perm[:])
                return
            
            for i in range(len(nums)):
                tmp = nums.pop(i)
                perm.append(tmp)
                backtracking(perm)
                perm.pop()
                nums.insert(i,tmp)

        backtracking([])
        return ans