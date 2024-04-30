class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n  # Handle the case where k is greater than or equal to the array length

    # Reverse the entire array
    self.reverse(nums, 0, n - 1)

    # Reverse the first k elements (new end)
    self.reverse(nums, 0, k - 1)

    # Reverse the remaining n - k elements (new beginning)
    self.reverse(nums, k, n - 1)

  def reverse(self, nums: List[int], start: int, end: int) -> None:  
    while start < end:
      nums[start], nums[end] = nums[end], nums[start]
      start += 1
      end -= 1