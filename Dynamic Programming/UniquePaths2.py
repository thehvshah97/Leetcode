from typing import List
import numpy as np


class UniquePaths2:
    def uniquePathsRecursion(self, m: int, n: int, obstacleGrid: List[List[int]]) -> int:
        if m == 0 or n == 0:
            return 1

        if obstacleGrid[m][n] == 1:
            return 0

        paths = 0
        for i in range(1, m):
            for j in range(1, n):
                paths += self.uniquePathsRecursion(i - 1, j, obstacleGrid) + self.uniquePathsRecursion(i, j - 1,
                                                                                                       obstacleGrid)
        return paths

    def uniquePathsMemoization(self, m: int, n: int, memoization: List[List[int]],
                               obstacleGrid: List[List[int]]) -> int:
        if m == 0 or n == 0:
            memoization[m][n] = 1
            return 1

        if obstacleGrid[m][n] == 1:
            memoization[m][n] = 0
            return 0

        if memoization[m][n] != -1:
            return memoization[m][n]

        paths = 0
        for i in range(1, m):
            for j in range(1, n):
                paths += self.uniquePathsRecursion(i - 1, j, obstacleGrid) + self.uniquePathsRecursion(i, j - 1,
                                                                                                       obstacleGrid)
        memoization[m][n] = paths
        return memoization[m][n]

    def uniquePathsTabulation(self, m: int, n: int, obstacleGrid: List[List[int]]) -> int:
        tabulation = np.zeros((m, n), int).tolist()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    tabulation[i][j] = 1

                elif obstacleGrid[i][j] == 1:
                    tabulation[i][j] = 0

                else:
                    tabulation[i][j] = tabulation[i - 1][j] + tabulation[i][j - 1]
        return tabulation[-1][-1]


if __name__ == '__main__':
    uniquePaths = UniquePaths2()
    print(uniquePaths.uniquePathsRecursion(2, 2, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    memoization = [[-1] * 3] * 3
    print(uniquePaths.uniquePathsMemoization(2, 2, memoization, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(uniquePaths.uniquePathsTabulation(3, 3, [[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
