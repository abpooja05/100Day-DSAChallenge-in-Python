#User function Template for python3
class Solution:
    def isDigitSumPalindrome(self, n):
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n = n // 10
            
        digit_sum_str = str(digit_sum)
        
        if digit_sum_str == digit_sum_str[::-1]:
            return 1
        else:
            return 0
            

# class Solution:
#     def isDigitSumPalindrome(self, n):
#         def digitsum(num):
#             total = 0
#             for digit in str(num):
#                 total += int(digit)
#             return total
            
#         def isPalindrome(num):
#             num_str = str(num)
#             return num_str == num_str[::-1]
            
#         digit_sum = digitsum(n)
#         if isPalindrome(digit_sum):
#             return 1
#         else:
#             return 0
       

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends