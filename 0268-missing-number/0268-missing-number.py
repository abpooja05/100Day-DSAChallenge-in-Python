class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_range = len(nums) + 1
        nums_set = set(nums)
        for num in range(0, nums_range):
            if num not in nums_set:
                return num
        return -1
           