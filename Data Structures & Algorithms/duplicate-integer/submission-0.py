class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seenNums = {}
        for i in nums:
            if i in seenNums:
                return True
            else:
                seenNums[i] = 1
        return False