#User function Template for python3

class Solution:
    def reverseEqn(self, s):
        # code here
        
        # num = ""
        # st = ""
        # for i in range(len(s)-1, -1, -1):
        #     if s[i].isdigit() == False:
        #         st += num[::-1] + s[i]
        #         num =""
        #     else:
        #         num += s[i]
        # st += num[::-1]
        # return st
        
        res_str = ""
        num = ""
        for c in s[::-1]:
            if c == '+' or c == '-' or c == '/' or c == '*':
                # reverse the number (incase of more than one digit)
                num = num[::-1]
                res_str += num
                num = ""
                
                # add in result
                res_str += c
            else:
                num += c
        
        # reverse the number (incase of more than one digit)
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
# } Driver Code Ends