class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest=arr[0]
        for i in arr:
            if i>largest:
                largest=i

        secondLargest=-1
        
        for i in arr:
            if i>secondLargest and i!=largest:
                secondLargest=i
                
        return secondLargest


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends