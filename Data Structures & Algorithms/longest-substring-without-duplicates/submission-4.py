class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        myDict = {}
        slow, fast = 0, 0
        length = 0

        while fast < len(s):
            if s[fast] in myDict:
                slow = max(myDict[s[fast]] + 1,slow)
            myDict[s[fast]] = fast
            length = max(length,fast - slow + 1)
            print(length)
            fast += 1
        return length