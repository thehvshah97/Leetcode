class ZigZagConversion:
    def convert(s: str, numRows: int) -> str:
        result =[]
        for currentElement in range(0,len(s)):
            for currentPosition in range (0,numRows):


        return result

if __name__ == '__main__':
    print(ZigZagConversion.convert("helloworld",3))
