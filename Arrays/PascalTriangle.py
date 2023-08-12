from typing import List

import numpy as np


class PascalTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1], [1, 1]]
        if numRows < 3:
            return dp[:numRows]
        for _ in range(2, numRows):
            next_row = [1]
            for i in range(1, len(dp[-1])):
                next_row.append(dp[-1][i] + dp[-1][i - 1])
            next_row += [1]
            dp.append(next_row)
        return dp


if __name__ == '__main__':
    pascalTriangle = PascalTriangle()
    print(pascalTriangle.generate(5))