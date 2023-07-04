from typing import List
import numpy as np

class RodCutting:
    def dynamicProgrammingTabulation(self, prices: List[int], length: int) -> int:
        dp = np.zeros([len(prices), length + 1], dtype=int)
        for i in range(length + 1):
            dp[0][i] = i * prices[0]

        for i in range(1, len(prices)):
            for j in range(length + 1):
                not_take = dp[i - 1][j]
                take = 0
                if i + 1 <= j:
                    take = dp[i][j - i - 1] + prices[i]
                dp[i][j] = max(take, not_take)
        print(dp)
        return dp[-1][-1]


if __name__ == '__main__':
    rodCutting = RodCutting()
    print(rodCutting.dynamicProgrammingTabulation([3, 5, 6, 7, 10, 12], 6))

