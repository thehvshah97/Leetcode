import math
from typing import List


class CoinChange2:
    def recursion(self, coins: List[int], index: int, target: int) -> int | float:
        if index == 0:
            if target % coins[index] == 0:
                return 1
            else:
                return 0
        elif target == 0:
            return 1
        elif target <= -1:
            return 0
        not_take = self.recursion(coins, index - 1, target)
        take = 0
        if coins[index] <= target:
            take = self.recursion(coins, index, target - coins[index])
        return take + not_take

    def recursionCalling(self, coins: List[int], amount: int) -> int:
        return self.recursion(coins, len(coins) - 1, amount)

    def dynamicProgrammingTabulation(self, coins: List[int], amount: int) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount + 1):
                if j % coins[i] == 0:
                    dp[i][j] += 1

        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                not_take = dp[i - 1][j]
                take = 0
                if coins[i] <= j:
                    take = dp[i][j - coins[i]]
                dp[i][j] = take + not_take
        return dp[len(coins) - 1][amount]


if __name__ == '__main__':
    coinChange = CoinChange2()
    print(coinChange.recursionCalling([1, 2, 5], 5))
    print(coinChange.dynamicProgrammingTabulation([2, 7, 13], 500))
