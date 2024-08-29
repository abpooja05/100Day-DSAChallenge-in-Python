#User function Template for python3

class Solution:
    def lcmAndGcd(self, A, B):
        
        x = A * B   # A is divident and B is divisor
        while B != 0:
            A, B = B, A%B
        return [x//A, A]
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends