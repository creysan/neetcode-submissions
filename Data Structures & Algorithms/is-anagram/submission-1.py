class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        if len(s) != len(t):
            return False
            
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        for letter in t:
            if letter not in letters:
                return False
        return True