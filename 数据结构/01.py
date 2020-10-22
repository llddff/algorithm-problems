def parchecker(s):
    stack = []
    balanced = True
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if not stack:
                balanced = False
            else:
                stack.pop()
    if balanced and not stack:
        return True
    else:
        return False


a = parchecker('()()')



def divideby2(number):
    stack = []
    while number > 0:
        rem = number % 2
        stack.append(rem)
        number >>= 1
    binString = ''
    while stack:
        binString += str(stack.pop())
    return binString


b = divideby2(633)

