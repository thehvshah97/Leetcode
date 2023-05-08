import numpy as np


class Knapsack:
    def recursion(self, items: list, values: list, weight: int, index: int, value: int) -> int:
        if index == 0:
            if items[0] <= weight:
                value += values[0]
            return value

        not_take = self.recursion(items, values, weight, index - 1, value)
        take = 0
        if items[index] <= weight:
            take = self.recursion(items, values, weight - items[index], index - 1, value + values[index])
        return max(take, not_take)

    def recursionCalling(self, items: list, values: list, weight: int) -> int:
        return self.recursion(items, values, weight, len(items) - 1, 0)

    def dynamicProgramming(self, items: list, values: list, weight: int, index: int, value: int,
                           dp: list) -> int:
        if index == 0:
            if items[0] <= weight:
                value += values[0]
            return value
        if dp[index][weight] != 0:
            return dp[index]
        not_take = self.dynamicProgramming(items, values, weight, index - 1, value, dp)
        take = 0
        if items[index] <= weight:
            take = self.dynamicProgramming(items, values, weight - items[index], index - 1, value + values[index], dp)
        dp[index][weight] = max(take, not_take)
        return dp[index][weight]

    def dynamicProgrammingCalling(self, items: list, values: list, weight: int) -> int:
        dp = np.zeros([len(items), weight + 1], dtype=int)
        return self.dynamicProgramming(items, values, weight, len(items) - 1, 0, dp)

    def dynamicProgrammingTabulation(self, items: list, values: list, weight: int):
        dp = np.zeros([len(items), weight + 1], dtype=int)
        for i in range(items[0], weight + 1):
            dp[0][i] = values[0]
        for i in range(1, len(items)):
            for j in range(weight + 1):
                not_take = dp[i - 1][j]
                take = 0
                if items[i] <= j:
                    take = dp[i - 1][j - items[i]] + values[i]
                dp[i][j] = max(take, not_take)
        return dp[-1][-1]


if __name__ == '__main__':
    knapsack = Knapsack()
    print(knapsack.recursionCalling([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack.dynamicProgrammingCalling([1, 2, 4, 5], [5, 4, 8, 6], 5))
    print(knapsack.dynamicProgrammingTabulation([1, 2, 4, 5], [5, 4, 8, 6], 5))

