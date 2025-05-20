class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(1 << n):  # 2^n combinations
            subset = []
            for j in range(n):
                if i & (1 << j):  # Check if j-th bit is set
                    subset.append(nums[j])
            res.append(subset)
        return res