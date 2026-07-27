class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsSeen = {}
        for i in nums:
            if i in numsSeen:
                return True
            else:
                numsSeen[i] = 1
        return False