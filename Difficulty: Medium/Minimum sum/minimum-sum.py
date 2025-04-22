#User function Template for python3

class Solution:
    def minSum(self, arr):
        # code here
        arr.sort()
        i = 0
        str1 = ""
        str2 = ""
        while i<len(arr):
            if arr[i]==0:
                i+=1
                continue
            if i&1==0:
                str1+=str(arr[i])
            else:
                str2+=str(arr[i])
            i+=1
        
        m = len(str1)-1
        n = len(str2)-1
        carry = 0
        res = ""
        while m>=0 and n>=0:
            total = int(str1[m])+int(str2[n])+carry
            value = total%10
            carry = total//10
            res = str(value) + res
            m-=1
            n-=1
        
        while m>=0:
            total = int(str1[m]) + carry
            value = total%10
            carry = total//10
            res = str(value) + res
            m-=1
        
        while n>=0:
            total = int(str2[n]) + carry
            value = total%10
            carry = total//10
            res = str(value) + res
            n-=1
        
        if carry>0:
            res = str(carry) + res
        
        return res

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends