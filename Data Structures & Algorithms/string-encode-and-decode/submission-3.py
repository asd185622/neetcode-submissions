class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ""
        for word in strs:
            length = len(word)
            encodedStr += str(length) + "#" + word
        print(encodedStr)
        return encodedStr
    def decode(self, s: str) -> List[str]:
        ans = []
        index = 0
        while index < len(s):
            length = ""
            while s[index] != "#":
                length += s[index]
                index += 1
            length = int(length)
            print(s[length])
            ans.append(s[index + 1:index + 1 + length])
            print(s[index + 1:index + 1 + length])
            index += (length + 1)
        return ans
