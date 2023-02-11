from typing import List


class MaximumEnergy:
    def maximize(self, m: list, th: int) -> int:
        m.sort(reverse=True)
        for i in range(0, m[0]):
            sum = 0
            for j in range(len(m)):
                temp = m[j] - i
                if temp > 0:
                    sum += temp
                else:
                    break
            if sum < th:
                return i


if __name__ == '__main__':
    uniquePaths = MaximumEnergy()
    print(uniquePaths.maximize([15, 7, 8, 19, 8], 1))
