class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # nums.sort()
        # ans = []

        # for i in range(len(nums)):
        #     #remove duplicates
        #     if i > 0 and nums[i] == nums[i - 1]:
        #         continue

        #     target = -1 * nums[i]
        #     j,k = i + 1, len(nums) - 1
        #     while j < k:

        #         if nums[j] + nums[k] > target:
        #             k -= 1
        #         elif nums[j] + nums[k] < target:
        #             j += 1
        #         else:
        #             ans.append([nums[i],nums[j],nums[k]])
        #             #remove j&k's duplicates
        #             while j < k and nums[j] == nums[j + 1]:
        #                 j += 1
        #             while j < k and nums[k] == nums[k - 1]:
        #                 k -= 1
                    
        #             j += 1
        #             k -= 1
        # return ans

        nums.sort()
        print(nums)
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = - nums[i]
            left = i  + 1
            right = len(nums) - 1
            # print(target,left,right)

            while left < right:
                # print(left,right)
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    while left < right and nums[left] == nums[left + 1]:
                        # print("left")
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        # print("right")
                        right -= 1
                    res.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
        return res

