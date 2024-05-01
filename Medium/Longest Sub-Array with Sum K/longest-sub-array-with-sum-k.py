#User function Template for python3

class Solution:
    def lenOfLongSubarr(self, arr, n, k): 
        prefix_sum = 0
        max_length = 0
        seen = {0: -1}  # Dictionary with Prefix_sum and their corresponding indices

        for i in range(n):
            prefix_sum += arr[i]

            if prefix_sum == k:
                max_length = max(max_length, i + 1)

            if (prefix_sum - k) in seen:
                current_length = i - seen[prefix_sum - k]
                max_length = max(max_length, current_length)

            if prefix_sum not in seen:
                seen[prefix_sum] = i

        return max_length



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends