from typing import List

import numpy as np


class MinimumPathSum:
    def minPathSumTabulation(self, grid: List[List[int]]) -> int:
        tabulation = np.zeros((len(grid), len(grid[0])), int).tolist()
        tabulation[0][0] = grid[0][0]
        for i in range(1, len(grid)):
            tabulation[i][0] = grid[i][0] + tabulation[i - 1][0]
        print(tabulation)
        for i in range(1, len(grid[0])):
            tabulation[0][i] = grid[0][i] + tabulation[0][i - 1]
        print(tabulation)
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                tabulation[i][j] = min(tabulation[i - 1][j], tabulation[i][j - 1]) + grid[i][j]
        return tabulation[-1][-1]


if __name__ == '__main__':
    minimumPathSum = MinimumPathSum()
    print(minimumPathSum.minPathSumTabulation([[1, 2], [1, 1]]))
