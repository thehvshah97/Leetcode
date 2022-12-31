class HouseRobber:
    def linear(self , val: list) -> int:
        even = 0
        odd = 0
        for i in range(len(val)):
            if i%2 == 0:
                even+=val[i]
            else:
                odd+=val[i]
        return max(even, odd)

if __name__ == '__main__':
    houseRobber = HouseRobber()
    val = [30, 10, 60, 10, 60, 50]
    print("Max Robbed:", houseRobber.linear(val))

