class BasicCalculator2:
    def calculate(self, s: str) -> int:
        if s == '' or s is None:
            return 0
        length = len(s)
        stack = []
        operation = '+'
        current_number = 0
        for i in range(length):
            current_char = s[i]
            if current_char.isnumeric():
                current_number = current_number * 10 + int(s[i])
            if not current_char.isnumeric() and not current_char.isspace() or i == length - 1:
                if operation == '-':
                    stack.append(-current_number)
                elif operation == '+':
                    stack.append(current_number)
                elif operation == '*':
                    stack.append(stack.pop() * current_number)
                elif operation == '/':
                    stack.append(int(stack.pop() / current_number))
                operation = current_char
                current_number = 0
        result = 0
        while stack:
            result += stack.pop()
        return result

if __name__ == '__main__':
    bc = BasicCalculator2()
    print(bc.calculate("3/2"))