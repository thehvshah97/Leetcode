from typing import List
import numpy as np


class UniquePaths:
    def uniquePathsRecursion(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 1

        paths = 0
        paths += self.uniquePathsRecursion(m - 1, n) + self.uniquePathsRecursion(m, n - 1)
        return paths

    def uniquePathsRecursionCalling(self, m: int, n: int) -> int:
        return self.uniquePathsRecursion(m - 1, n - 1)
    
    def uniquePathsMemoization(self, m: int, n: int, memoization: List[List[int]]) -> int:
        if m == 0 or n == 0:
            memoization[m][n] = 1
            return memoization[m][n]

        if memoization[m][n] != 0:
            return memoization[m][n]

        paths = 0
        for i in range(1, m):
            for j in range(1, n):
                paths += self.uniquePathsMemoization(i - 1, j, memoization) + self.uniquePathsMemoization(i, j - 1,
                                                                                                          memoization)
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
    print(uniquePaths.uniquePathsRecursionCalling(2, 3))
    memoization = np.zeros((3, 4), int).tolist()
    print(uniquePaths.uniquePathsMemoization(2, 3, memoization))
    print(uniquePaths.uniquePathsTabulation(2, 3))
