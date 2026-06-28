class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeat = set()
        for num in nums:
            if num in repeat:
                return num
            repeat.add(num)
        return -1