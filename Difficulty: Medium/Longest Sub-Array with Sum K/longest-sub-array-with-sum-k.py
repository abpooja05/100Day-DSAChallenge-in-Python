#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        #Complete the function
        prefix_sum = 0
        max_length = 0
        sum_index_map = {0: -1}  # This handles the case where the sum starts from index 0

        for i in range(len(arr)):
            prefix_sum += arr[i]

            if (prefix_sum - k) in sum_index_map:
                subarray_length = i - sum_index_map[prefix_sum - k]
                max_length = max(max_length, subarray_length)

            if prefix_sum not in sum_index_map:
                sum_index_map[prefix_sum] = i

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