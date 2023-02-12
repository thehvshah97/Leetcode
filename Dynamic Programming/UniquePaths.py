from typing import List
import numpy as np


class UniquePaths:
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
    print(uniquePaths.uniquePathsTabulation(2, 3))
