class Solution:
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxNum, minNum, minIdx = max(nums), min(nums), 0
        for i in range(1, len(nums)):
            if [nums[i-1], nums[i]] == [maxNum, minNum]:
                minIdx = i                
                break
        return nums[minIdx:] + nums[:minIdx] == sorted(nums)
    
    ###other method
#     def check(self, nums: List[int]) -> bool:
#         n = len(nums)
#         # Find the pivot point where the rotation occurs
#         pivot = 0
#         for i in range(1, n):
#             if nums[i] < nums[i - 1]:
#                 pivot = i
#                 break
        
#         # Check if the array is sorted in non-decreasing order after rotation
#         for i in range(1, n):
#             if nums[(pivot + i) % n] < nums[(pivot + i - 1) % n]:
#                 return False
#         return True
