class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans, product, j = 0, 1, 0  # Initialize variables

        for i in range(len(nums)):
            product *= nums[i]  # Update product with current element

            # Shrink the window while product is greater than or equal to k
            while j <= i and product >= k:
                product //= nums[j]  # Divide product by the element leaving the window
                j += 1

            # Count all subarrays ending at index i (including the empty subarray)
            ans += i - j + 1  # This is the key calculation

        return ans