import math
from typing import List


class CoinChange:
    def recursion(self, coins: List[int], index: int, target: int) -> int | float:
        if index == 0:
            if target % coins[index] == 0:
                return int(target / coins[index])
            else:
                return 1e9
        if target == 0:
            return 0
        not_take = self.recursion(coins, index - 1, target)
        take = math.inf
        if coins[index] <= target:
            take = 1 + self.recursion(coins, index, target - coins[index])
        return min(take, not_take)

    def recursionCalling(self, coins: List[int], amount: int) -> int:
        return self.recursion(coins, len(coins) - 1, amount)

    def dynamicProgramming(self, coins: List[int], index: int, target: int, dp: List[List[int]]) -> int | float:
        if index == 0:
            if target % coins[index] == 0:
                return int(target / coins[index])
            else:
                return int(1e9)
        if target == 0:
            return 0
        if dp[index][target] != -1:
            return dp[index][target]
        not_take = self.dynamicProgramming(coins, index - 1, target, dp)
        take = math.inf
        if coins[index] <= target:
            take = 1 + self.dynamicProgramming(coins, index, target - coins[index], dp)
        dp[index][target] = min(take, not_take)
        return dp[index][target]

    def dynamicProgrammingCalling(self, coins: List[int], amount: int) -> int:
        dp = [[-1 for j in range(amount + 1)] for i in range(len(coins))]
        return self.dynamicProgramming(coins, len(coins) - 1, amount, dp)

    def dynamicProgrammingTabulation(self, coins: List[int], amount: int) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        for i in range(amount + 1):
            if i % coins[0] == 0:
                dp[0][i] = i // coins[0]
            else:
                dp[0][i] = int(1e9)
        for i in range(1, len(coins)):
            for j in range(1, amount + 1):
                not_take = 0 + dp[i - 1][j]
                take = 1e9
                if coins[i] <= j:
                    take = 1 + dp[i][j - coins[i]]
                dp[i][j] = min(take, not_take)
        ans = dp[len(coins) - 1][amount]
        if ans >= int(1e9):
            return -1
        return ans


if __name__ == '__main__':
    coinChange = CoinChange()
    print(coinChange.recursionCalling([1, 2, 5], 11))
    print(coinChange.dynamicProgrammingCalling([1, 2, 5], 11))
    print(coinChange.dynamicProgrammingTabulation([2, 5, 10, 1], 27))
