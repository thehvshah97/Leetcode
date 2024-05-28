from typing import List


class Item:
    def __init__(self, weight: int, value: int):
        self.weight = weight
        self.value = value
        self.fractional_value = value/weight


class FractionalKnapsack:
    def greedy(self, weights: List[int], values: List[int], max_weight: int) -> int:
        items = [Item(weights[i], values[i]) for i in range(len(weights))]
        sorted(items, key=lambda x: x.fractional_value)
        max_profit = 0
        i = 0
        while max_weight > 0:
            if items[i].weight <= max_weight:
                max_profit += items[i].value
                max_weight -= items[i].weight
                i += 1
            else:
                max_profit += (items[i].fractional_value * max_weight)
                max_weight -= max_weight
                break
        return max_profit


if __name__ == '__main__':
    fractional_knapsack = FractionalKnapsack()
    print(fractional_knapsack.greedy([10, 20, 30], [60, 100, 120], 50))