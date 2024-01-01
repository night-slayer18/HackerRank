def evaluate_prefix_expression(expression):
    stack = []
    operators = {'+', '-', '*', '^'}
    operations = {
        '+': lambda a, b: a + b,
        '-': lambda a, b: a - b,
        '*': lambda a, b: a * b,
        '^': lambda a, b: a ** b
    }

    for char in reversed(expression.split()):
        if char.isdigit():
            stack.append(int(char))
        elif char in operators:
            operand1 = stack.pop()
            operand2 = stack.pop()
            stack.append(operations [char](operand1, operand2))
        else:
            print("expression evaluation stopped invalid words present", end="")
            return

    if len(stack) != 1:
        print("expression is not complete or invalid", end="")
        return

    return stack.pop()

inp = input()
inp = inp.replace("c","")
inp = inp.replace("one","1")
inp = inp.replace("two","2")
inp = inp.replace("three","3")
inp = inp.replace("four","4")
inp = inp.replace("five","5")
inp = inp.replace("six","6")
inp = inp.replace("seven","7")
inp = inp.replace("eight","8")
inp = inp.replace("nine","9")
inp = inp.replace("zero","0")
inp = inp.replace("add","+")
inp = inp.replace("sub","-")
inp = inp.replace("mul","*")
inp = inp.replace("mod","%")
inp = inp.replace("pow","^")

result = evaluate_prefix_expression(inp)
if result is not None:
    print(result, end="")


