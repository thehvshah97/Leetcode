from typing import List


class BuyAndSellStocks4:
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

    def recursionCalling(self, prices: List[int], transactions: int) -> int:
        return self.recursion(prices, 0, True, transactions)

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

    def dynamicProgrammingMemoizationCalling(self, prices: List[int], transactions: int) -> int:
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(len(prices) + 1)]
        return self.dynamicProgrammingMemoization(prices, 0, 1, transactions, dp)

    def dynamicProgrammingTabulation(self, prices: List[int], transactions: int) -> int:
        dp = [[[0 for _ in range(transactions + 1)] for _ in range(2)] for _ in range(len(prices) + 1)]
        for index in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, transactions + 1):
                    if buy == 1:
                        dp[index][buy][cap] = max(dp[index + 1][1][cap], dp[index + 1][0][cap] - prices[index])
                    else:
                        dp[index][buy][cap] = max(dp[index + 1][1][cap - 1] + prices[index], dp[index + 1][0][cap])
        return dp[0][1][transactions]

    def dynamicProgrammingTabulationSpaceOptimized(self, prices: List[int], transactions: int):
        ahead = [[0 for _ in range(transactions + 1)] for _ in range(2)]
        curr = [[0 for _ in range(transactions + 1)] for _ in range(2)]
        for index in range(len(prices) - 1, -1, -1):
            for buy in range(2):
                for cap in range(1, transactions + 1):
                    if buy == 1:
                        curr[buy][cap] = max(ahead[1][cap], ahead[0][cap] - prices[index])
                    else:
                        curr[buy][cap] = max(ahead[1][cap - 1] + prices[index], ahead[0][cap])
            ahead = curr
        return curr[1][2]


if __name__ == '__main__':
    buyAndSellStocks4 = BuyAndSellStocks4()
    print(buyAndSellStocks4.recursionCalling([2, 4, 1], 2))
    print(buyAndSellStocks4.dynamicProgrammingMemoizationCalling([2, 4, 1], 2))
    print(buyAndSellStocks4.dynamicProgrammingTabulation([2, 4, 1], 2))
    print(buyAndSellStocks4.dynamicProgrammingTabulationSpaceOptimized([2, 4, 1], 2))
