class Solution:
    def rowWithMax1s(self, arr):
        # code here
        n = len(arr)
        if n == 0:
            return -1
        m = len(arr[0])
        max_count = 0
        result_row = -1
        
        for i in range(n):
            # Using binary search to find the first occurrence of 1 in the current row
            left, right = 0, m - 1
            first_one = m  # Initialize with the number of columns (no 1s)
            
            while left <= right:
                mid = (left + right) // 2
                if arr[i][mid] == 1:
                    first_one = mid
                    right = mid - 1
                else:
                    left = mid + 1
            
            count = m - first_one
            if count > max_count:
                max_count = count
                result_row = i
            elif count == max_count and result_row == -1:
                result_row = i
        
        return result_row if max_count != 0 else -1


#{ 
 # Driver Code Starts
# Main execution starts here
if __name__ == "__main__":
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        input_line = input().strip()  # Read input matrix as string
        mat = eval(input_line)  # Convert string to matrix

        solution = Solution()
        result = solution.rowWithMax1s(mat)  # Get the row with the most 1s

        print(result)
        print("~")

# } Driver Code Ends