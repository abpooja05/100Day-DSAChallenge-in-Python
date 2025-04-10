#User function Template for python3

class Solution:
    def getTable(self,n):
        # code here
        table = []
        for i in range(1, 11):
            res = table.append(i*n)
        return table

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        ans = ob.getTable(n)
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends