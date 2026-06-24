class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(k):
            time = 0
            for i in piles:
                time += (i + k - 1) // k
            if time > h:
                return False
            else:
                return True

        l, r = 1, max(piles)
        ans = 0

        while l <= r:
            mid = (l + r) // 2

            if canFinish(mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans