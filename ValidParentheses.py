class ValidParentheses:
    def validparentheses(s: str) -> bool:
        dict ={"{":"}","[":"]","(":")"}
        parantheses = list(s)
        stack=[]
        for bracket in parantheses:
            if bracket in ["[", "{", "("]:
                stack.append(bracket)
            elif bracket in ["]", "}", ")"]:
                if len(stack) == 0 or bracket != dict[stack.pop()]:
                    return False
        if len(stack) !=0:
            return False
        else:
            return True

if __name__ == '__main__':
    print(ValidParentheses.validparentheses(""))
