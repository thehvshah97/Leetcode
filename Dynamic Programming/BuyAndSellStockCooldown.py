from typing import List


class BuyAndSellStocksCooldown:
    def recursion(self, prices: List[int], index: int, buy:bool) -> int:
        if index >= len(prices) - 1:
            if not buy:
                return prices[index]
            else:
                return 0

        if buy:
            not_bought = self.recursion(prices, index + 1, True)
            bought = self.recursion(prices, index + 1, False) - prices[index]
            return max(not_bought, bought)
        else:
            sell = self.recursion(prices, index + 2, True) + prices[index]
            not_sell = self.recursion(prices, index + 1, False)
            return max(sell, not_sell)

    def recursionCalling(self, prices: List[int]) -> int:
        return self.recursion(prices, 0, True)

    def dynamicProgrammingMemoization(self, prices: List[int], index: int, buy: int, dp: List[List[int]]) -> int:
        if index >= len(prices) - 1:
            if buy == 0:
                return prices[index]
            else:
                return 0

        if dp[index][buy] != -1:
            return dp[index][buy]

        if buy == 1:
            not_bought = self.dynamicProgrammingMemoization(prices, index + 1, 1, dp)
            bought = self.dynamicProgrammingMemoization(prices, index + 1, 0, dp) - prices[index]
            dp[index][buy] = max(not_bought, bought)
        else:
            sell = self.dynamicProgrammingMemoization(prices, index + 2, 1, dp) + prices[index]
            not_sell = self.dynamicProgrammingMemoization(prices, index + 1, 0, dp)
            dp[index][buy] = max(sell, not_sell)
        return dp[index][buy]

    def dynamicProgrammingMemoizationCalling(self, prices: List[int]):
        dp = [[-1 for _ in range(2)] for _ in range(len(prices) + 1)]
        return self.dynamicProgrammingMemoization(prices, 0, 1, dp)

    def dynamicProgrammingTabulation(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 2)]
        for index in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                if buy == 1:
                    dp[index][buy] = max(dp[index + 1][1], dp[index + 1][0] - prices[index])
                else:
                    dp[index][buy] = max(dp[index + 2][1] + prices[index], dp[index + 1][0])
        return dp[0][1]


if __name__ == '__main__':
    buyAndSellStocksCooldown = BuyAndSellStocksCooldown()
    print(buyAndSellStocksCooldown.recursionCalling([1, 2, 3, 0, 2]))
    print(buyAndSellStocksCooldown.dynamicProgrammingMemoizationCalling([1, 2, 3, 0, 2]))
    print(buyAndSellStocksCooldown.dynamicProgrammingTabulation([1, 2, 3, 0, 2]))