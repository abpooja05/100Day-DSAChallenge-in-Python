#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


#User function Template for python3

class Solution:
    def mergeSort(self,arr, l, r):
        def merge(arr,l,m,r):
            temp=[]
            start=l
            end=m+1
            while start<=m and end<=r:
                if arr[start]<=arr[end]:
                    temp.append(arr[start])
                    start+=1
                else:
                    temp.append(arr[end])
                    end+=1
            while start<=m:
                temp.append(arr[start])
                start+=1
            while end<=r:
                temp.append(arr[end])
                end+=1
            for i in range(l,r+1):
                arr[i]=temp[i-l]
            return arr
        if l>=r:
            return
        mid=(l+r)//2
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        merge(arr,l,mid,r)
                
                
        



#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ob.mergeSort(arr,0,len(arr)-1)
        print(*arr)
        print("~")
        t -= 1


# } Driver Code Ends