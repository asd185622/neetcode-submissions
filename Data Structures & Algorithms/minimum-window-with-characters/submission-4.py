class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        wordDict = {}
        tDict = {}
        have = 0
        need = len(t)
        left, right = 0, 0

        resLeft, resRight = 0, 0
        resL = float('inf')
        for c in t:
            wordDict[c] = 0
            tDict[c] = tDict.get(c,0) + 1

        for i in range(len(s)):
            if s[i] in tDict:
                wordDict[s[i]] += 1
                if wordDict[s[i]] <= tDict[s[i]]:
                    have += 1
            
            while have == need:
                # print(have,need)
                if right - left + 1 < resL:
                    resLeft, resRight = left, right
                    resL = resRight - resLeft + 1
                if s[left] in wordDict:
                    wordDict[s[left]] -= 1
                    if wordDict[s[left]] < tDict[s[left]]:
                        have -= 1
                left += 1
            right += 1
        
        return s[resLeft:resRight + 1] if resL != float('inf') else ""