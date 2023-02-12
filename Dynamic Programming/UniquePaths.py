from typing import List
import numpy as np


class UniquePaths:
    def uniquePathsRecursion(self, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 1
        return self.uniquePathsRecursion(m - 1, n) + self.uniquePathsRecursion(m, n - 1)

    def uniquePathsRecursionCalling(self, m: int, n: int) -> int:
        return self.uniquePathsRecursion(m - 1, n - 1)

    def uniquePathsMemoization(self, m: int, n: int, memoization: List[List[int]]) -> int:
        if m == 0 or n == 0:
            memoization[m][n] = 1
            return memoization[m][n]
        elif memoization[m][n] != 0:
            return memoization[m][n]

        paths = 0
        paths += self.uniquePathsMemoization(m - 1, n, memoization) + self.uniquePathsMemoization(m, n - 1, memoization)
        memoization[m][n] = paths
        return memoization[m][n]

    def uniquePathsMemoizationCalling(self, m: int, n: int) -> int:
        memoization = np.zeros((m, n), int).tolist()
        return uniquePaths.uniquePathsMemoization(m - 1, n - 1, memoization)

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
    print(uniquePaths.uniquePathsMemoizationCalling(2, 3))
    print(uniquePaths.uniquePathsTabulation(2, 3))
