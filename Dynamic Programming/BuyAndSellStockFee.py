from typing import List


class BuyAndSellStocksFee:
    def dynamicProgrammingTabulation(self, prices: List[int], fee: int) -> int:
        dp = [[0 for _ in range(2)] for _ in range(len(prices) + 2)]
        for index in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                if buy == 1:
                    dp[index][buy] = max(dp[index + 1][1], dp[index + 1][0] - prices[index])
                else:
                    dp[index][buy] = max(dp[index + 1][1] + prices[index] - fee, dp[index + 1][0])
        return dp[0][1]


if __name__ == '__main__':
    buyAndSellStocksFee = BuyAndSellStocksFee()
    print(buyAndSellStocksFee.dynamicProgrammingTabulation([1, 3, 2, 8, 4, 9], 2))
