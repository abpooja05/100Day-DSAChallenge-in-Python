class Solution:
  def sortColors(self, nums: List[int]) -> None:
    """
        Do not return anything, modify nums in-place instead.
        """

    # Initialize pointers for red (low) and blue (high) ends
    low = 0
    high = len(nums) - 1
    i = 0  # Current index being processed

    # Iterate while the current index is less than or equal to the high pointer
    while i <= high:
      # If the current element is red (0), swap it with the element at the low index
      # and increment both low and current indices
      if nums[i] == 0:
        nums[i], nums[low] = nums[low], nums[i]
        low += 1
        i += 1
      # If the current element is blue (2), swap it with the element at the high index
      # and decrement the high index only (current index remains the same)
      elif nums[i] == 2:
        nums[i], nums[high] = nums[high], nums[i]
        high -= 1
      # If the current element is white (1), simply increment the current index
      else:
        i += 1        