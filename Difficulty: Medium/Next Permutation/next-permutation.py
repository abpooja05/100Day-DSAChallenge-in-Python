#User function Template for python3

class Solution:
    def nextPermutation(self, N, arr):
        # Step 1: Find the largest index i such that arr[i] < arr[i + 1]
        i = N - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        if i >= 0:  # If such index i is found
            # Step 2: Find the largest index j such that arr[i] < arr[j]
            j = N - 1
            while arr[j] <= arr[i]:
                j -= 1
            
            # Step 3: Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
        
        # Step 4: Reverse the sequence from arr[i + 1] to the end
        arr[i + 1:] = reversed(arr[i + 1:])
        
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends