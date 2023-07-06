from typing import List

import numpy as np


class UnboundedKnapsack:
    def recursion(self, items: list, values: list, weight: int, index: int, value: int, item: int) -> int:
        if index == 0:
            if item != 0:
                return self.recursion(items, values, weight - items[0], 0, value + values[0], item - 1)
            elif items[0] <= weight:
                value += values[0]
            return value
        if item == 0:
            return value
        not_take = self.recursion(items, values, weight, index - 1, value, item)
        take = 0
        if items[index] <= weight:
            take = self.recursion(items, values, weight - items[index], index, value + values[index], item - 1)
        return max(take, not_take)

    def recursionCalling(self, items: list, values: list, weight: int, item: int) -> int:
        return self.recursion(items, values, weight, len(items) - 1, 0, item)

    def dynamicProgrammingMemoization(self, items: list, values: list, weight: int, index: int, value: int, item: int, dp: List[List[int]]) -> int:
        if index == 0:
            if item != 0:
                return self.recursion(items, values, weight - items[0], 0, value + values[0], item - 1)
            elif items[0] <= weight:
                value += values[0]
            return value
        if item == 0:
            return value
        if dp[index][weight] != 0:
            return dp[index][weight]
        not_take = self.dynamicProgrammingMemoization(items, values, weight, index - 1, value, item, dp)
        take = 0
        if items[index] <= weight:
            take = self.dynamicProgrammingMemoization(items, values, weight - items[index], index, value + values[index], item - 1, dp)
        dp[index][weight] = max(take, not_take)
        return dp[index][weight]

    def dynamicProgrammingMemoizationCalling(self, items: list, values: list, weight: int, item: int) -> int:
        dp = np.zeros([len(items), weight + 1], dtype=int)
        return self.dynamicProgrammingMemoization(items, values, weight, len(items) - 1, 0, item, dp)

    def dynamicProgrammingTabulation(self, items: List[int], values: List[int], weight: int, item: int) -> int:
        dp = np.zeros([len(items), weight + 1], dtype=int)
        for i in range(weight + 1):
            dp[0][i] = (i // items[0]) * values[0]

        for i in range(1, item):
            for j in range(weight + 1):
                not_take = dp[i - 1][j]
                take = 0
                if items[i] <= j:
                    take = dp[i][j - items[i]] + values[i]
                dp[i][j] = max(take, not_take)
        return dp[-1][-1]

    def dynamicProgrammingTabulationSpace(self, items: List[int], values: List[int], weight: int, item: int) -> int:
        dp = np.zeros(weight + 1, dtype=int)
        for i in range(weight + 1):
            dp[i] = (i // items[0]) * values[0]

        for i in range(1, item):
            for j in range(weight + 1):
                not_take = dp[j]
                take = 0
                if items[i] <= j:
                    take = dp[j - items[i]] + values[i]
                dp[j] = max(take, not_take)
        return dp[-1]


if __name__ == '__main__':
    knapsack = UnboundedKnapsack()
    print(knapsack.recursionCalling([5, 10, 20], [7, 2, 4], 15, 3))
    print(knapsack.dynamicProgrammingMemoizationCalling([5, 10, 20], [7, 2, 4], 15, 3))
    print(knapsack.dynamicProgrammingTabulation([5, 10, 20], [7, 2, 4], 15, 3))
    print(knapsack.dynamicProgrammingTabulationSpace([5, 10, 20], [7, 2, 4], 15, 3))

