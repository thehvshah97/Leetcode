class FrogKJumps:
    def recursion(self, val: list, index: int, jump: int) -> int:
        if index == 0:
            return 0
        energy = [50000] * jump
        for i in range(1, jump+1):
            if index - i >= 0:
                energy[i-1] = self.recursion(val, index - i, jump) + abs(val[index] - val[index - i])
        return min(energy)

    def dynamicProgramming(self, val: list, index: int, jump: int) -> int:
        energy = [-1] * len(val)
        for i in range(0, len(val)):
            if i == 0:
                energy[i] = 0
            else:
                jumpEnergy = [50000] * (jump+1)
                for j in range(1, jump+1):
                    if i - j >= 0:
                        jumpEnergy[j] = energy[i-j] + abs(val[i] - val[i-j])
                energy[i] = min(jumpEnergy)
        return energy[len(val) - 1]


if __name__ == '__main__':
    frogKJump = FrogKJumps()
    val = [30, 10, 60, 10, 60, 50]
    jumps = 5
    print("Energy Expended:", frogKJump.recursion(val, len(val) - 1, jumps))
    print("Energy Expended dynamic Programming:", frogKJump.dynamicProgramming(val, len(val) - 1, jumps))


