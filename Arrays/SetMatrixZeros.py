from typing import List

class SetMatrixZeros:
    def setMatrixZeros(self, matrix: List[List[int]]):
        temp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    temp[i][j] = 0
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if temp[i][j] == 0:
                    for x in range(len(matrix[0])):
                        matrix[i][x] = 0
                    for x in range(len(matrix)):
                        matrix[x][j] = 0

    def setmatrixZerosOptimized(self, matrix: List[List[int]]):
        rows = [-1] * len(matrix)
        columns = [-1] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    rows[i] = 0
                    columns[j] = 0

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if rows[i] == 0 or columns[j] == 0:
                    matrix[i][j] = 0

if __name__ == '__main__':
    setMatrixZeros = SetMatrixZeros()
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setMatrixZeros.setMatrixZeros(matrix)
    print(matrix)
    #optimized
    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    setMatrixZeros.setmatrixZerosOptimized(matrix)
    print(matrix)


