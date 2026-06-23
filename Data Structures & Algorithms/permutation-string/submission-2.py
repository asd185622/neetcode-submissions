class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freq = [0] * 26
        freq2 = [0] * 26
        size = len(s1)
        l, r = 0, size - 1
        #initialize the freq
        for i in range(size):
            freq[ord(s1[i]) - ord('a')] += 1
            freq2[ord(s2[i]) - ord('a')] += 1

        while r < len(s2):
            if freq2 == freq:
                return True
            elif r != len(s2) - 1:
                r += 1
                freq2[ord(s2[r]) - ord('a')] += 1
                freq2[ord(s2[l]) - ord('a')] -= 1
                l += 1
            else:
                break
        return False