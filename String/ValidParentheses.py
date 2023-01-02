class ValidParentheses:
    def validParentheses(s: str) -> bool:
        dictionary = {"{": "}", "[": "]", "(": ")"}
        parenthesis = list(s)
        stack = []
        for bracket in parenthesis:
            if bracket in ["[", "{", "("]:
                stack.append(bracket)
            elif bracket in ["]", "}", ")"]:
                if len(stack) == 0 or bracket != dictionary[stack.pop()]:
                    return False
        if len(stack) !=0:
            return False
        else:
            return True


if __name__ == '__main__':
    print(ValidParentheses.validParentheses(""))
