class Solution:
    def countPair(self, k, arr):
        # Initialize pointers and count
        left = 0
        right = len(arr) - 1
        count = 0
        
        # Two-pointer approach
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == k:
                count += 1
                left += 1
                right -= 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1
        
        return count



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    import sys
    input = sys.stdin.read
    data = input().split('\n')

    t = int(data[0].strip())
    index = 1

    for _ in range(t):
        k = int(data[index].strip())
        index += 1
        arr = list(map(int, data[index].strip().split()))
        index += 1

        res = Solution().countPair(k, arr)
        print(res)


if __name__ == "__main__":
    main()

# } Driver Code Ends