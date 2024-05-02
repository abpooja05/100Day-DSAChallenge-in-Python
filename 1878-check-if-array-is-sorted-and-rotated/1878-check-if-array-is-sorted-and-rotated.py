class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        # Find the pivot point where the rotation occurs
        pivot = 0
        for i in range(1, n):
            if nums[i] < nums[i - 1]:
                pivot = i
                break
        
        # Check if the array is sorted in non-decreasing order after rotation
        for i in range(1, n):
            if nums[(pivot + i) % n] < nums[(pivot + i - 1) % n]:
                return False
        return True
