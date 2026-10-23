'''
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    else:
        return 0
def is_right_associative(op):
        return op == '^'
def infix_to_postfix(expression): 
    stack = []
    postfix = []
    for char in expression:
        if char.isalnum():
            postfix.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while (stack and precedence(stack[-1]) >= precedence(char) and not is_right_associative(char)):
                postfix.append(stack.pop())
            stack.append(char)
    while stack:
        postfix.append(stack.pop())
    return ''.join(postfix)
test_cases = [
    "A+B*C",   
    "(A+B)*C",
    "A+B*(C^D-E)",
    "A+B*(C^D-E)^(F+G*H)-I"
]
for expression in test_cases:
    postfix = infix_to_postfix(expression)
    print(f"Infix: {expression} => Postfix: {postfix}")
'''
def evaluate_postfix(expression):
    stack = []
    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                stack.append(a + b)
            elif char == '-':
                stack.append(a - b)
            elif char == '*':
                stack.append(a * b)
            elif char == '/':
                stack.append(a / b)
            elif char == '^':
                stack.append(a ** b)
    return stack[0]
test_cases = [
    "23*54*+9-",
    "82/3-32*+",
    "34+5*6-", 
    "56+78+*9-"
]
for expression in test_cases:
    result = evaluate_postfix(expression)
    print(f"Postfix: {expression} => Result: {result}")
