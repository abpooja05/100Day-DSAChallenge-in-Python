#User function Template for python3
class Solution:
    def largestPrimeFactor (self, N):
        # code here
        i = 2
        # For a non-prime number n, there will be at least one factor <= sqrt(n)
        while i*i <= N:
            if N % i == 0:
                N = N // i
            else:
                i += 1
        return N
        
        # prime_factor = 1
        # i = 2
        # while i <= N:
        #     if N % i == 0:
        #         prime_factor = i
        #         N = N/i
        #     else:
        #         i += 1
        
        # if prime_factor < N:
        #     prime_factor = N
        # else:
        #     return prime_factor
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.largestPrimeFactor(N))
# } Driver Code Ends