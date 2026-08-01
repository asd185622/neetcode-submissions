class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtracking(comb,left,right):
            if left == n and right == n:
                ans.append("".join(comb))
                return
            if left < n:
                comb.append('(')
                backtracking(comb,left + 1,right)
                comb.pop()
            if left > right:
                comb.append(')')
                backtracking(comb,left,right + 1)
                comb.pop()

        backtracking([],0,0)
        return ans