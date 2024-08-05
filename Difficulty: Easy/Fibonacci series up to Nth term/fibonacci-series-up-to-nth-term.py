#User function Template for python3

class Solution:
    
    def __init__(self):
        self.memo = {}

    def fibonacci(self, n):
        MOD = 10**9 + 7
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        if n == 1:
            return 1
        self.memo[n] = (self.fibonacci(n - 1) + self.fibonacci(n - 2)) % MOD
        return self.memo[n]

    def series(self, n):
        if n == 0:
            return [0]
        result = []
        for i in range(n + 1):
            result.append(self.fibonacci(i))
        return result
    
    # def series(self, n):
       
        # if n == 0:
        #     return [0]  # Special case for n = 0

        # mod = 10**9 + 7  # Modulo value

        # # Initialize first two terms
        # a, b = 0, 1

        # # Create a list to store the Fibonacci series
        # fib_series = [a % mod, b % mod]

        # # Loop to calculate and store remaining terms
        # for i in range(2, n + 1):
        #     c = (a + b) % mod  # Calculate next term with modulo
        #     fib_series.append(c)
        #     a, b = b, c  # Update for next iteration

        # return fib_series
        
        ### other method
        # prev = 0
        # res = [0, 1]
        # for i in range(1,n):
        #     res.append((res[-1]+res[-2])%(10**9 + 7))
        # return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        result = ob.series(N)
        print(*result)
# } Driver Code Ends