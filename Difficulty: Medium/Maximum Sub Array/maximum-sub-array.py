#User function Template for python3

class Solution:

    def findSubarray(self, n, a):
        max_sum = -1
        max_start = -1
        max_end = -1
        current_sum = 0
        current_start = 0

        for i in range(n):
            if a[i] >= 0:
                current_sum += a[i]
                if current_sum > max_sum or (current_sum == max_sum and i - current_start > max_end - max_start):
                    max_sum = current_sum
                    max_start = current_start
                    max_end = i
            else:
                current_sum = 0
                current_start = i + 1

        if max_sum == -1:
            return [-1]
        else:
            return a[max_start:max_end + 1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findSubarray(n, a)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1

# } Driver Code Ends