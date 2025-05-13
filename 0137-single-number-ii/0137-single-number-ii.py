class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):
            count = 0
            for num in nums:
                # Check if the i-th bit is set
                if (num >> i) & 1:
                    count += 1
            # Set the bit in result if count is not divisible by 3
            if count % 3 != 0:
                if i == 31:
                    # Handle negative numbers by subtracting 2^31
                    result -= (1 << 31)
                else:
                    result |= (1 << i)
        return result
        