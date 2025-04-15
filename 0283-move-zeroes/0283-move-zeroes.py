class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l = 0  # initialise left pointer
        for r in range(len(nums)):  # right pointer iterates through length of array
            if nums[r]:   # If num is non-zero swap the left and right pointer values
                nums[l], nums[r] = nums[r], nums[l]
                l += 1  # increment left pointer everytime you swap the values
        return nums