#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        res_str = ""
        num = ""
        
        for c in s[::-1]:
            if c == "+" or c == "-" or c == "/" or c == "*":
                num = num[::-1] #if "c" is a two or more digit number
                res_str += num
                num = ""
                
                #add in the result
                res_str += c
                
            else:
                num += c
                
        num = num[::-1]
        res_str += num
        return res_str
                

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
        print("~")
# } Driver Code Ends