class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda x: (len(x), x))  # Sort by numeric value
        return nums[-k]