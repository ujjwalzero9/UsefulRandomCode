def golmine(grid):
    m, n = len(grid), len(grid[0])
    dp = [row[:] for row in grid]
    
    for j in range(n):
        dp[0][j] = grid[0][j]
        
    for j in range(1, n):
        dp[0][j] = max(dp[0][j], grid[0][j-1] + grid[0][j], grid[1][j-1] + grid[0][j])
        
    for j in range(1, n):
        dp[m-1][j] = max(dp[m-1][j], grid[m-1][j-1] + grid[m-1][j], grid[m-2][j-1] + grid[m-1][j])
        
    for i in range(1, m - 1):
        for j in range(1, n):
            dp[i][j] = max(dp[i][j], dp[i][j-1] + grid[i][j], dp[i-1][j-1] + grid[i][j], dp[i+1][j-1] + grid[i][j])
    
    return max(dp[i][n-1] for i in range(m))
if __name__ == "__main__":
    grid = [
        [1, 3, 3],
        [2, 1, 4],
        [0, 6, 4]
    ]
    print("Max gold collected:", golmine(grid))
