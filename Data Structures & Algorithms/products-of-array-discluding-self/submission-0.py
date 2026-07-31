class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * len(nums)
        i = 1
        while i < len(nums):
            left[i] = left[i - 1] * nums[i - 1]
            i += 1
        j = len(nums) - 1
        right = 1
        while j >= 0:
            left[j] *= right
            right *= nums[j]
            j -= 1
        return left