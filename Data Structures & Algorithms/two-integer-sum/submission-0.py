class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = {}
        # [3, 4, 5, 6]
        for i, n in enumerate(nums):
            # for 0,1,2,3 and 3,4,5,6
            diff = target - n
            # diff = 7 - 3 = 4
            # diff = 7 - 4 = 3
            if diff in total:
                return [total[diff], i]
                # return [0, 1]
            total[n] = i
            # {3: 0}