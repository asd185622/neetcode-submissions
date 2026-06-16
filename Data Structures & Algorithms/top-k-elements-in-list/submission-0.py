class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}
        ans = []

        #get each number's frequency
        for num in nums:
            frequency[num] = frequency.get(num,0) + 1
        #grouping number's frequency
        group = {}
        for key,value in frequency.items():
            if value not in group:
                group[value] = [key]
            else:
                group[value].append(key)
        
        while k > 0:
            maxFrequen = -1
            for key in group:
                if key > maxFrequen:
                    maxFrequen = key
            
            for num in group[maxFrequen]:
                ans.append(num)
            k -= len(group[maxFrequen])
            del group[maxFrequen]
        
        return ans
        