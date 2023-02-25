import math
from typing import List
import numpy as np


class UniquePathsTriangle:
    def uniquePathsRecursion(self, grid: List[List[int]], level: int, position: int) -> int:
        if level == len(grid) - 1:
            return grid[level][position]

        down = grid[level][position] + self.uniquePathsRecursion(grid, level + 1, position)
        diagonal = grid[level][position] + self.uniquePathsRecursion(grid, level + 1, position + 1)
        return min(down, diagonal)

    def uniquePathsRecursionCalling(self, grid: List[List[int]]) -> int:
        return self.uniquePathsRecursion(grid, 0, 0)

    def uniquePathsMemoization(self, grid: List[List[int]], level: int, position: int,
                               memoization: List[List[int]]) -> int:
        if level == len(grid) - 1:
            return grid[level][position]
        elif memoization[level][position] != 0:
            return memoization[level][position]
        down = grid[level][position] + self.uniquePathsMemoization(grid, level + 1, position, memoization)
        diagonal = grid[level][position] + self.uniquePathsMemoization(grid, level + 1, position + 1, memoization)
        memoization[level][position] = min(down, diagonal)
        return memoization[level][position]

    def uniquePathsMemoizationCalling(self, grid: List[List[int]]) -> int:
        memoization = np.zeros((len(grid) + 1, len(grid[len(grid) - 1]) + 1), int).tolist()
        return self.uniquePathsMemoization(grid, 0, 0, memoization)

    def uniquePathsTabulation(self, grid: List[List[int]]) -> int:
        tabulation = np.zeros((len(grid), len(grid[len(grid) - 1])), int).tolist()
        for i in range(len(grid[len(grid) - 1])):
            tabulation[len(grid) - 1][i] = grid[len(grid) - 1][i]
        for i in range(len(grid) - 2, -1, -1):
            for j in range(i, -1, -1):
                down = grid[i][j] + tabulation[i + 1][j]
                diagonal = grid[i][j] + tabulation[i + 1][j + 1]
                tabulation[i][j] = min(down, diagonal)
        return tabulation[0][0]


if __name__ == '__main__':
    uniquePaths = UniquePathsTriangle()
    print(uniquePaths.uniquePathsRecursionCalling([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(uniquePaths.uniquePathsMemoizationCalling(
        [[-7], [-2, 1], [-5, -5, 9], [-4, -5, 4, 4], [-6, -6, 2, -1, -5], [3, 7, 8, -3, 7, -9],
         [-9, -1, -9, 6, 9, 0, 7], [-7, 0, -6, -8, 7, 1, -4, 9], [-3, 2, -6, -9, -7, -6, -9, 4, 0],
         [-8, -6, -3, -9, -2, -6, 7, -5, 0, 7], [-9, -1, -2, 4, -2, 4, 4, -1, 2, -5, 5],
         [1, 1, -6, 1, -2, -4, 4, -2, 6, -6, 0, 6], [-3, -3, -6, -2, -6, -2, 7, -9, -5, -7, -5, 5, 1]]))
    print(uniquePaths.uniquePathsTabulation([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
