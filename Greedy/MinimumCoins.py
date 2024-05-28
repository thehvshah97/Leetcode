from typing import List


class MinimumCoins:
    def greedy(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        number_of_coins = 0
        i = 0
        while amount > 0:
            coin, amount = divmod(amount, coins[i])
            number_of_coins += coin
            i += 1
            if i > len(coins):
                return -1
        return number_of_coins


if __name__ == '__main__':
    print(MinimumCoins().greedy([1, 2, 5, 10, 20, 50, 100, 200, 500, 1000], 121))