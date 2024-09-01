#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

import math
class Solution:
    def print_divisors(self, N):
        # code here
        l1 = []
        l2 = []
        for i in range(1, int(N ** 0.5)+1):
            if N % i == 0:
                l1.append(i)
                if N // i != i:
                    l2.append(N//i)
                    
        res = l1 + l2[::-1]
        for i in res:
            print(i, end=" ")

# class Solution:
#     def print_divisors(self, N):
#         # code here
#         divisors = []
#         for i in range(1, int(N ** 0.5)+ 1):
#             if N % i == 0:
#                 divisors.append(i)
#                 if N // i != 0:
#                     divisors.append(N//i)
        
        
#         # divisors.sort()
#         for divisor in sorted(divisors):
#             print(divisor, end=' ')
            
            
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
# } Driver Code Ends