#User function Template for python3

class Solution:
    def armstrongNumber(self, n):
        first = n % 10
        second = (n // 10) % 10
        third = n // 100
        digit_sum = first ** 3 + second ** 3 + third ** 3

        return n == digit_sum
        
        

#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        flag = ob.armstrongNumber(n)
        if flag:
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends