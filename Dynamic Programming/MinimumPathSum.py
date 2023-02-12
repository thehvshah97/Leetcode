from typing import List
import numpy as np

class MinimumPathSum:
    def minPathSumRecursion(self, m: int, n: int, grid: List[List[int]]) -> int:
        if m == 0 and n == 0:
            return grid[0][0]
        elif m == 0:
            return grid[m][n - 1] + grid[m][n]
        elif n == 0:
            return grid[m - 1][n] + grid[m][n]
        return min(self.minPathSumRecursion(m - 1, n, grid), self.minPathSumRecursion(m, n - 1, grid)) + grid[m][n]

    def minPathSumRecursionCalling(self, grid: List[List[int]]) -> int:
        return self.minPathSumRecursion(len(grid) - 1, len(grid[0]) - 1, grid)

    def minPathSumMemoization(self, m: int, n: int, grid: List[List[int]], memoization: List[List[int]]) -> int:
        if m == 0 and n == 0:
            return grid[0][0]
        elif m == 0:
            return grid[m][n - 1] + grid[m][n]
        elif n == 0:
            return grid[m - 1][n] + grid[m][n]
        elif memoization[m][n] != 0:
            return memoization[m][n]
        memoization[m][n] = min(self.minPathSumRecursion(m - 1, n, grid), self.minPathSumRecursion(m, n - 1, grid)) + \
                            grid[m][n]
        return memoization[m][n]

    def minPathSumMemoizationCalling(self, grid: List[List[int]]) -> int:
        memoization = np.zeros((len(grid), len(grid[0])), int).tolist()
        return self.minPathSumMemoization(len(grid) - 1, len(grid[0]) - 1, grid, memoization)

    def minPathSumTabulation(self, grid: List[List[int]]) -> int:
        tabulation = np.zeros((len(grid), len(grid[0])), int).tolist()
        tabulation[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            tabulation[i][0] = grid[i][0] + tabulation[i - 1][0]
        for i in range(1, len(grid[0])):
            tabulation[0][i] = grid[0][i] + tabulation[0][i - 1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                tabulation[i][j] = min(tabulation[i - 1][j], tabulation[i][j - 1]) + grid[i][j]
        return tabulation[-1][-1]


if __name__ == '__main__':
    minimumPathSum = MinimumPathSum()
    print(minimumPathSum.minPathSumRecursionCalling([[1, 2], [1, 1]]))
    print(minimumPathSum.minPathSumMemoizationCalling([[1, 2], [1, 1]]))
    print(minimumPathSum.minPathSumTabulation([[1, 2], [1, 1]]))
