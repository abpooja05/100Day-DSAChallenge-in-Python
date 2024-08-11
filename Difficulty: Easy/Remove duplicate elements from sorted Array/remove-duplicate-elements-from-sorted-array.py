class Solution:
    def remove_duplicate(self, arr):
        # If the array is empty, return 0
        if not arr:
            return 0
        
        # Pointer to place the next unique element
        index = 1
        
        # Traverse the array starting from the second element
        for i in range(1, len(arr)):
            # If the current element is different from the previous one
            if arr[i] != arr[i - 1]:
                arr[index] = arr[i]
                index += 1
        
        # The length of the modified array with distinct elements
        return index


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.remove_duplicate(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()

# } Driver Code Ends