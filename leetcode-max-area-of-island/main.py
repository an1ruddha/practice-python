from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = []
        len_row = len(grid)
        len_col = len(grid[0])
        
        def check(grid, row, col):
            if not 0<=row<len_row or not 0<=col<len_col or not grid[row][col]:
                return 0
            else:
                grid[row][col] = 0
                return 1 + check(grid, row, col - 1,) + \
                        check(grid, row, col + 1) + \
                        check(grid, row - 1, col) + \
                        check(grid, row + 1, col)

        for row in range(len_row):
            for col in range(len_col):
                area.append(check(grid, row, col))
        return max(area)

def main():
    obj = Solution()
    list_grid = [[[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]],
                 [[0,0,0,0,0,0,0,0]]]
    
    for grid in list_grid:
        print(obj.maxAreaOfIsland(grid), " = ", grid)
if __name__ == "__main__":
    main()

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

