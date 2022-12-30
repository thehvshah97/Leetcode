class FrogJump:
    def recursion(self, val: list, index: int) -> int:
        if index == 0:
            return 0
        left = self.recursion(val, index - 1) + abs(val[index]-val[index - 1])
        if index > 1:
            right = self.recursion(val, index - 2) + abs(val[index]-val[index - 2])
            return min(left, right)
        else:
            return left

    def dynamicProgramming(self, val: list, index: int) -> int:
        energy = [-1] * len(val)
        for i in range(0, len(val)):
            if i == 0:
                energy[i] = 0
            else:
                left = energy[i-1] + abs(val[i] - val[i-1])
                if i > 1:
                    right = energy[i-2] + abs(val[i] - val[i-2])
                    if left < right:
                        energy[i] = left
                    else:
                        energy[i] = right
                else:
                    energy[i] = left
        return energy[len(val) - 1]


if __name__ == '__main__':
    frogJump = FrogJump()
    val = [30, 10, 60, 10, 60, 50]
    print("Minimum Energy:", frogJump.recursion(val, len(val)-1))
    print("Minimum Energy dynamic Programming:", frogJump.dynamicProgramming(val, len(val) - 1))
