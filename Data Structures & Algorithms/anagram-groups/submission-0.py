class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagram = {}

        for word in strs:
            tmp = [0] * 26
            for char in word:
                tmp[ord(char) - ord('a')] += 1
            tmp = tuple(tmp)
            if tmp in anagram:
                anagram[tmp].append(word)
            else:
                anagram[tmp] = [word]
        
        for value in anagram.values():
            ans.append(value)

        return ans
            