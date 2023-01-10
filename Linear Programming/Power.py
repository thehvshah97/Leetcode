class Power:
    def myPowNaive(self, x: float, n: int) -> float:
        ans = x
        for i in range(1, n):
            ans *= x
        return ans

    def myPowOptimized(self, x: float, n: int) -> float:
        ans = 1.0
        current_power = n
        if current_power < 0:
            current_power *= -1
        while current_power:
            if current_power % 2:
                ans *= x
                current_power -= 1
            else:
                x *= x
                current_power /= 2

        if n < 0:
            ans = 1.0 / ans
        return ans


if __name__ == '__main__':
    power = Power()
    print(power.myPowOptimized(2.5, 3))
