import math
from typing import List
import numpy as np


class UniquePathsTriangle:
    def uniquePathsRecursion(self, grid: List[List[int]], level: int, position: int, path: int) -> int:
        if level == len(grid) - 1:
            return path + grid[level][position]

        path += grid[level][position]
        return min(self.uniquePathsRecursion(grid, level + 1, position, path),
                   self.uniquePathsRecursion(grid, level + 1, position + 1, path))

    def uniquePathsRecursionCalling(self, grid: List[List[int]]) -> int:
        return self.uniquePathsRecursion(grid, 0, 0, 0)

    def uniquePathsMemoization(self, grid: List[List[int]], level: int, position: int, path: int,
                               memoization: List[List[int]]) -> int:
        if level == len(grid) - 1:
            return path + grid[level][position]
        elif memoization[level][position] != 0:
            return memoization[level][position]
        path += grid[level][position]
        memoization[level][position] = min(self.uniquePathsMemoization(grid, level + 1, position, path, memoization),
                                           self.uniquePathsMemoization(grid, level + 1, position + 1, path,
                                                                       memoization))
        return memoization[level][position]

    def uniquePathsMemoizationCalling(self, grid: List[List[int]]) -> int:
        memoization = np.zeros((len(grid) + 1, len(grid[len(grid) - 1]) + 1), int).tolist()
        return self.uniquePathsMemoization(grid, 0, 0, 0, memoization)


if __name__ == '__main__':
    uniquePaths = UniquePathsTriangle()
    print(uniquePaths.uniquePathsRecursionCalling([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
    print(uniquePaths.uniquePathsMemoizationCalling([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))
