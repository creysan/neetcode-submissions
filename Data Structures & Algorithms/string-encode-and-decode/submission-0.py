class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in strs:
            encodedString += str(len(i)) + "#" + i
        return encodedString

    def decode(self, s: str) -> List[str]:
        decodedStrs = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                
            length = int(s[i:j])
            contentStart = j + 1
            contentEnd = contentStart + length
            content = s[contentStart:contentEnd]
            decodedStrs.append(content)
            i = contentEnd
        return decodedStrs
