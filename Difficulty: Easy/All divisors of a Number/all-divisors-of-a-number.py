#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def print_divisors(self, N):
        smaller = []
        larger = []
        
        i = 1
        while i * i <= N:
            if N % i == 0:
                smaller.append(i)
                if i != N // i:
                    larger.append(N // i)
            i += 1
        
        for num in smaller:
            print(num, end=" ")
        for num in reversed(larger):
            print(num, end=" ")
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ob = Solution()
        ob.print_divisors(N)
        print()
        print("~")
# } Driver Code Ends