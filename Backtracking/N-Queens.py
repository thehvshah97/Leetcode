from typing import List

class NQueens:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        result = []
        columns = set()
        diagonalPositive = set()
        diagonalNegative = set()

        def backtrack(row):
            if row == n:
                resCopy = ["".join(row) for row in board]
                result.append(resCopy)
                return

            for col in range(n):
                if col in columns or (row + col) in diagonalPositive or (row - col) in diagonalNegative:
                    continue

                columns.add(col)
                diagonalPositive.add(row + col)
                diagonalNegative.add(row - col)
                board[row][col] = "Q"
                backtrack(row + 1)

                columns.remove(col)
                diagonalPositive.remove(row + col)
                diagonalNegative.remove(row - col)
                board[row][col] = "."
        backtrack(0)
        return result


if __name__ == "__main__":
    nQueens = NQueens()
    print(nQueens.solveNQueens(9))
