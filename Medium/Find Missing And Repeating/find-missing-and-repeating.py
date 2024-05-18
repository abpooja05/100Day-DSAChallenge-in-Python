#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        expected_sum = n * (n+1) // 2
        expected_sum_squares = n * (n+1) * (2* n+1) // 6
        
        actual_sum = sum(arr)
        actual_sum_squares = sum(x*x for x in arr)
        
        sum_diff = expected_sum - actual_sum
        sum_squares_diff = expected_sum_squares - actual_sum_squares
        
        missing_plus_repeating = sum_squares_diff // sum_diff
        
        missing = (sum_diff + missing_plus_repeating) // 2
        repeating = missing_plus_repeating - missing
            
        return [repeating, missing]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends