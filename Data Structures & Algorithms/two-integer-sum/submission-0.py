class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myDict = {}

        for index,num in enumerate(nums):
            tmp = target - num
            if tmp not in myDict:
                myDict[num] = index
            else:
                if myDict[tmp] > index:
                    return [index, myDict[tmp]]
                else:
                    return [myDict[tmp], index]

        