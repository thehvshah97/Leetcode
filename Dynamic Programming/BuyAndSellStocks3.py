from typing import List


class BuyAndSellStocks3:
    def recursion(self, prices: List[int], index: int, buy: bool, cap: int) -> int:
        if cap == 0:
            return 0

        if index == len(prices) - 1:
            if not buy:
                return prices[index]
            else:
                return 0

        if buy:
            not_bought = self.recursion(prices, index + 1, True, cap)
            bought = self.recursion(prices, index + 1, False, cap) - prices[index]
            return max(not_bought, bought)
        else:
            sell = self.recursion(prices, index + 1, True, cap - 1) + prices[index]
            not_sell = self.recursion(prices, index + 1, False, cap)
            return max(sell, not_sell)

    def recursionCalling(self, prices: List[int]) -> int:
        return self.recursion(prices, 0, True, 2)

    def dynamicProgrammingMemoization(self, prices: List[int], index: int, buy: int, cap: int, dp: List[List[List[int]]]) -> int:
        if cap == 0:
            return 0

        if index == len(prices) - 1:
            if buy == 0:
                return prices[index]
            else:
                return 0

        if dp[index][buy][cap] != -1:
            return dp[index][buy][cap]

        if buy == 1:
            not_bought = self.dynamicProgrammingMemoization(prices, index + 1, 1, cap, dp)
            bought = self.dynamicProgrammingMemoization(prices, index + 1, 0, cap, dp) - prices[index]
            dp[index][buy][cap] = max(not_bought, bought)
        else:
            sell = self.dynamicProgrammingMemoization(prices, index + 1, 1, cap - 1, dp) + prices[index]
            not_sell = self.dynamicProgrammingMemoization(prices, index + 1, 0, cap, dp)
            dp[index][buy][cap] = max(sell, not_sell)
        return dp[index][buy][cap]

    def dynamicProgrammingMemoizationCalling(self, prices: List[int]):
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices) + 1)]
        return self.dynamicProgrammingMemoization(prices, 0, 1, 2, dp)

    def dynamicProgrammingTabulation(self, prices: List[int]) -> int:
        dp = [[[0 for _ in range(3)] for _ in range(2)] for _ in range(len(prices) + 1)]
        for index in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 1:
                        dp[index][buy][cap] = max(dp[index + 1][1][cap], dp[index + 1][0][cap] - prices[index])
                    else:
                        dp[index][buy][cap] = max(dp[index + 1][1][cap - 1] + prices[index], dp[index + 1][0][cap])
        return dp[0][1][2]

    def dynamicProgrammingTabulationSpaceOptimized(self, prices: List[int]):
        ahead = [[0 for _ in range(3)] for _ in range(2)]
        curr = [[0 for _ in range(3)] for _ in range(2)]
        for index in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, 3):
                    if buy == 1:
                        curr[buy][cap] = max(ahead[1][cap], ahead[0][cap] - prices[index])
                    else:
                        curr[buy][cap] = max(ahead[1][cap - 1] + prices[index], ahead[0][cap])
            ahead = curr
        return curr[1][2]


if __name__ == '__main__':
    buyAndSellStocks3 = BuyAndSellStocks3()
    print(buyAndSellStocks3.recursionCalling([3, 3, 5, 0, 0, 3, 1, 4]))
    print(buyAndSellStocks3.dynamicProgrammingMemoizationCalling([3, 3, 5, 0, 0, 3, 1, 4]))
    print(buyAndSellStocks3.dynamicProgrammingTabulation([3, 3, 5, 0, 0, 3, 1, 4]))
    print(buyAndSellStocks3.dynamicProgrammingTabulationSpaceOptimized([3, 3, 5, 0, 0, 3, 1, 4]))
