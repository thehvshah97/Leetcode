class ClimbingStairs:
    def climbing_stairs_recursion(self, stairs: int, index: int) -> int:
        if index == stairs:
            return 1
        elif index > stairs:
            return 0

        return self.climbing_stairs_recursion(stairs, index + 1) + self.climbing_stairs_recursion(stairs, index + 2)

    def climbing_stairs_tabulation(self, stairs: int) -> int:
        dp = [0 for _ in range(stairs + 2)]
        dp[stairs] = 1
        for i in range(stairs - 1, -1, -1):
            dp[i] = dp[i + 1] + dp[i + 2]
        return dp[0]


if __name__ == '__main__':
    climbingStairs = ClimbingStairs()
    print(climbingStairs.climbing_stairs_recursion(3, 0))
    print(climbingStairs.climbing_stairs_tabulation(3))
