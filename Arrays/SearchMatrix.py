import math
from typing import List


class SearchMatrix:
    def searchMatrixNaive(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if matrix[i][len(matrix[0]) - 1] >= target:
                for j in range(len(matrix[0])):
                    if matrix[i][j] == target:
                        return True
        return False

    def searchMatrixOptimized(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        left = 0
        right = n * m - 1
        while left <= right:
            mid = int((left + right) / 2)
            number = matrix[mid // m][mid % m]
            if target == number:
                return True
            elif target < number:
                right = mid
            else:
                left = mid + 1
        return False

    def searchMatrixFlatten(self, matrix: [List[List[int]]], target: int) -> bool:
        matrix = [j for sub in matrix for j in sub]
        left = 0
        right = len(matrix)
        while left <= right:
            mid = int((left + right) / 2)
            if matrix[mid] == target:
                return True
            elif target < matrix[mid]:
                right = mid
            else:
                left = mid + 1
        return False


if __name__ == '__main__':
    searchMatrix = SearchMatrix()
    print(searchMatrix.searchMatrixNaive([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(searchMatrix.searchMatrixOptimized([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
    print(searchMatrix.searchMatrixFlatten([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
