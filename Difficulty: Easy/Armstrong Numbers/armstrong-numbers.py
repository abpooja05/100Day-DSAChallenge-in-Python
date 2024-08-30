#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here 
        first = n // 100
        second = (n // 10) % 10
        third = n % 10
        
        total = first ** 3 + second ** 3 + third ** 3
        if n == total:
            return "true"
        else:
            return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends