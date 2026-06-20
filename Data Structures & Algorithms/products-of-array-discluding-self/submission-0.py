class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        suffix = []

        products = 1
        for num in nums:
            prefix.append(products)
            products *= num
        
        products = 1
        for num in nums[::-1]:
            suffix.insert(0,products)
            products *= num
        
        print(f"prefix: {prefix}")
        print(f"suffix: {suffix}")

        ans = []
        for i in range(len(prefix)):
            ans.append(prefix[i] * suffix[i])
        
        return ans