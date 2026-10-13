class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        ROW = len(board)
        COL = len(board[0])
        valid = []
        cur = set()
        is_good = True

        def dfs(i,j):
            nonlocal is_good

            if min(i,j) < 0 or i >= ROW or j >= COL or board[i][j] == 'X' or (i,j) in cur:
                return

            if (i,j) in visited:
                return

            if board[i][j] == 'O' and (i == 0 or j == 0 or i == ROW -1 or j == COL-1):
                is_good = False

            cur.add((i,j))
            visited.add((i,j))

            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i+1, j)
            dfs(i, j-1)

        for i in range(ROW):
            for j in range(COL):
                if board[i][j] == "O" and (i,j) not in visited:
                    dfs(i,j)
                    if is_good:
                        valid.append(cur.copy())
                    cur.clear()
                    is_good = True
        
        for e in valid:
            for r,c in e:
                board[r][c] = 'X'
