class GoodArray:
    def goodArray(self, n: int, queries: list) -> list:
        v = []
        res = []
        result = []
        print("Blocks for %d : " % n, end="")
        while n > 0:
            v.append(int(n % 2))
            n = int(n / 2)

        for i in range(len(v)):
            if v[i] == 1:
                res.append(pow(2, i))

        for query in queries:
            mul = 1
            l = query[0]
            r = query[1]
            for i in range(l-1, r):
                mul *= res[i]
            print(mul)
            mod = mul % query[2]
            result.append(mod)
        return result


if __name__ == '__main__':
    goodArray = GoodArray()
    print(goodArray.goodArray(26, [[1, 2, 1009], [3, 3, 5]]))

