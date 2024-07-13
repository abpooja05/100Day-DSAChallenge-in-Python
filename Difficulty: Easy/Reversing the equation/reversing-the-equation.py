#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        
        num = ""
        st = ""
        for i in range(len(s)-1, -1, -1):
            if s[i].isdigit() == False:
                st += num[::-1] + s[i]
                num =""
            else:
                num += s[i]
        st += num[::-1]
        return st
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        ob = Solution()
        ans = ob.reverseEqn(s)
        print(ans)
# } Driver Code Ends