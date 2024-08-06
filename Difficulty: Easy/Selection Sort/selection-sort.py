#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        minindex = i
        for j in range(i+1, n):
            if arr[j] < arr[minindex]:
                minindex = j
        return minindex
    
    def selectionSort(self, arr, n):
        #code here
        for i in range(n):
            minindex = self.select(arr, i)
            
            arr[i], arr[minindex] = arr[minindex], arr[i]
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends