from typing import List
import numpy as np


class UniquePaths:
    def uniquePathsRecursion(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 1

        paths = 0
        for i in range(1, m):
            for j in range(1, n):
                paths += self.uniquePathsRecursion(i-1, j) + self.uniquePathsRecursion(i, j-1)
        return paths

    def uniquePathsMemoization(self, m: int, n: int, memoization: List[List[int]]) -> int:
        if m == 0 or n == 0:
            memoization[m][n] = 1
            return memoization[m][n]

        if memoization[m][n] != -1:
            return memoization[m][n]
        paths = 0
        for i in range(1, m):
            for j in range(1, n):
                paths += self.uniquePathsRecursion(i-1, j) + self.uniquePathsRecursion(i, j-1)
        memoization[m][n] = paths
        return memoization[m][n]

    def uniquePathsTabulation(self, m: int, n: int) -> int:
        tabulation = np.zeros((m, n), int).tolist()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    tabulation[i][j] = 1
                else:
                    tabulation[i][j] = tabulation[i - 1][j] + tabulation[i][j - 1]
        return tabulation[-1][-1]


if __name__ == '__main__':
    uniquePaths = UniquePaths()
    print(uniquePaths.uniquePathsRecursion(2, 3))
    memoization = [[-1] * (3 + 1)] * (2 + 1)
    print(uniquePaths.uniquePathsMemoization(2, 3, memoization))
    print(uniquePaths.uniquePathsTabulation(2, 3))
