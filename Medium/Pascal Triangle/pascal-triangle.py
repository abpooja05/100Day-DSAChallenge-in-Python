#User function Template for python3
class Solution:
    def nthRowOfPascalTriangle(self, n):
        MOD = 10**9 + 7
        
        # Initialize the Pascal's triangle with first row
        pascal_triangle = [[1]]
        
        # Generate Pascal's triangle up to the Nth row
        for i in range(1, n):
            row = [1]  # First element of each row is always 1
            for j in range(1, i):
                # Calculate each element based on the previous row
                row.append((pascal_triangle[i - 1][j - 1] + pascal_triangle[i - 1][j]) % MOD)
            row.append(1)  # Last element of each row is always 1
            pascal_triangle.append(row)
        
        # Return the Nth row of Pascal's triangle
        return pascal_triangle[n - 1]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends