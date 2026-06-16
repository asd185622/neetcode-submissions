class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check = set()

        for num in nums:
            if num not in check:
                check.add(num)
            else:
                return True
        return False
        