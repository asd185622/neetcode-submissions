class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        # print(candidates)

        def backtracking(comb,val,start):
            if val > target:
                return
            if val == target:
                ans.append(comb[:])
                return
            
            for i in range(start,len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                comb.append(candidates[i])
                val += candidates[i]
                backtracking(comb,val,i + 1)
                comb.pop()
                val -= candidates[i]
        
        backtracking([],0,0)
        return ans