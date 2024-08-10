#User function Template for python3

class Solution:
    def merge(self, arr, l, m, r):
        # Lengths of the two sub-arrays
        len1 = m - l + 1
        len2 = r - m
        
        # Create temporary arrays
        first = arr[l:m+1]
        second = arr[m+1:r+1]
        
        # Initialize indices
        index1 = 0
        index2 = 0
        mainarrayindex = l
        
        # Merge the two arrays
        while index1 < len1 and index2 < len2:
            if first[index1] <= second[index2]:
                arr[mainarrayindex] = first[index1]
                index1 += 1
            else:
                arr[mainarrayindex] = second[index2]
                index2 += 1
            mainarrayindex += 1
        
        # Copy any remaining elements from the first array
        while index1 < len1:
            arr[mainarrayindex] = first[index1]
            index1 += 1
            mainarrayindex += 1
        
        # Copy any remaining elements from the second array
        while index2 < len2:
            arr[mainarrayindex] = second[index2]
            index2 += 1
            mainarrayindex += 1
        
    def mergeSort(self, arr, l, r):
        if l < r:
            # Find the middle point
            m = (l + r) // 2
            
            # Sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            
            # Merge the sorted halves
            self.merge(arr, l, m, r)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends