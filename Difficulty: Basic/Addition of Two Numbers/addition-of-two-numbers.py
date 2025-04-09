#User function Template for python3
class Solution:
    def addition (ob, a, b):
        # code here 
        res = a+b
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        A, B = map(int, input().strip().split(" "))

        ob = Solution()
        print(ob.addition(A, B))
        print("~")

# } Driver Code Ends