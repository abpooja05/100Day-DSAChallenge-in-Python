#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, arr, n, k):
        #Code here
        n = len(arr)
        prod = 1
        res = 0
        l = 0
        r = 0
        while r < n:
            prod *= arr[r]
            while l < r and prod >= k :
                prod = int(prod//arr[l])
                l += 1
            if prod < k:
                res += (r-l+1)
            r += 1
        
        return res
                
                
    
    
    
 
    
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]

        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends