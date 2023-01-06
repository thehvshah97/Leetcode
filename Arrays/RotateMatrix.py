from typing import List
import numpy as np

class RotateMatrix:
    def rotateMatrix(self, matrix: List[List[int]]) -> object:
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


if __name__ == '__main__':
    rotateMatrix = RotateMatrix()
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotateMatrix.rotateMatrix(matrix)
    print(matrix)

