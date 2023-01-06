from typing import List


class MaxIceCreamBars:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        number = 0
        for c in costs:
            if c <= coins:
                coins -= c
                number += 1
            else:
                break
        return number


if __name__ == '__main__':
    maxIceCreamBars = MaxIceCreamBars()
    print(maxIceCreamBars.maxIceCream([1, 3, 2, 4, 1], 7))

