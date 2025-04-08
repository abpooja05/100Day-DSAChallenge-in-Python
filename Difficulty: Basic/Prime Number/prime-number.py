#User function Template for python3

class Solution:
    def isPrime(self, n):
        # code here
        if n <= 1:
            return 0
            
        if n <= 3:
            return 1
            
        if n % 2 == 0 or n % 3 == 0:
            return 0
            
        i = 5
        while i*i <= n:
            if n % i == 0 or n%(i+2) == 0:
                return 0
            i += 6
        return 1

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())  # Read number of test cases
    for _ in range(t):
        n = int(input())  # Read the number to check primality

        ob = Solution()
        # Using Python's conditional expression for true/false
        print("true" if ob.isPrime(n) else
              "false")  # Print "true" if prime, else "false"
        print("~")

# } Driver Code Ends