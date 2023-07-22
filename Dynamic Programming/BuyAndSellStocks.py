from typing import List


class BuyAndSellStocks:
    def buyAndSellStocks(self, prices: List[int]) -> int:
        maxProfit = 0
        minVal = prices[0]
        for i in range(1, len(prices)):
            minVal = min(minVal, prices[i])
            maxProfit = max(maxProfit, prices[i] - minVal)
        return maxProfit


if __name__ == '__main__':
    buyAndSell = BuyAndSellStocks()
    print(buyAndSell.buyAndSellStocks([7, 1, 5, 3, 6, 4]))

