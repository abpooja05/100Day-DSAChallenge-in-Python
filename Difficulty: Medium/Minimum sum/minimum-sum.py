#User function Template for python3

class Solution:
    def solve(self, arr, n):
        # code here
        if n==1:
            return(str(arr[0]))
        
        arr.sort()
        
        num1=""
        num2=""
        
        for i in range(n):
            if i%2==0:
                num1+=str(arr[i])
            else:
                num2+=str(arr[i])
                
        sum1=int(num1)+int(num2)
        return(sum1)

# class Solution:
#   def solve(self,arr, n):
 
#     # sort the array
#     arr.sort()
 
#     # let two numbers be a and b
#     a = 0
#     b = 0
#     for i in range(n):
 
#         # Fill a and b with every alternate
#         # digit of input array
#         if (i % 2 != 0):
#             a = a * 10 + arr[i]
#         else:
#             b = b * 10 + arr[i]
 
#     # return the sum
#     return a + b

#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.solve(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends