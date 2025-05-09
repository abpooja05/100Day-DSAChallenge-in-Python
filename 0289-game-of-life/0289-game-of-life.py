class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        m, n = len(board), len(board[0])
        
        # Directions to check the eight neighbors
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1),  (1, 0), (1, 1)]
        
        # First pass to mark the cells that will change
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and (board[ni][nj] == 1 or board[ni][nj] == -1):
                        live_neighbors += 1
                
                # Rule 1 or 3: Cell dies (mark as -1 if currently alive)
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1
                # Rule 4: Cell becomes alive (mark as 2 if currently dead)
                elif board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2
        
        # Second pass to update the board
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1