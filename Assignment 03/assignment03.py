from pythonds.basic.stack import Stack


def infixToPostfix(infixexpr):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    opStack = Stack()
    postfixList = []
    tokenList = list(infixexpr)

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower() or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
               (prec[opStack.peek()] >= prec[token]):
                  postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)


def get_value_from_output(token):
    with open('output.txt') as rf:
        for line in rf:
            line = line.strip()
            if '=' in line:
                var, value = tuple(line.split('='))
                if token == var:
                    return value


def postfixEval(postfixExpr):
    operandStack = Stack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        elif token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower():
            operandStack.push(int(get_value_from_output(token)))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token, operand1, operand2)
            operandStack.push(result)
    return operandStack.pop()


def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2


def sub_error(index, exp):
    if index == len(exp) -1:
        return True
    character = exp[index+1]
    if character in '*+/-':
        return True


def check_error(expression):
    # check for ;
    if expression[-1] != ';':
        return True
    # check for '('
    if expression.count('(') != expression.count(')'):
        return True
    formatted_exp = expression[:-1]
    for i, cha in enumerate(formatted_exp):
        if cha in '+-*/':
            if sub_error(i, formatted_exp):
                return True
        if cha is '(':
            if sub_error(i, formatted_exp):
                return True
    return False


def write_in_file(line):
    line += '\n'
    with open('output.txt', 'a') as af:
        af.write(line)
    return


def is_expression(mystr):
    operators = list('+-/*()')
    if any(cha in operators for cha in mystr):
        return True
    return False


with open('input.txt') as rf:
    for line in rf:
        line = line.strip()
        if '=' not in line:

            if check_error(line):
                print('Error!!')
                break

            line = line[:-1]
            if not is_expression(line):
                write_in_file(line)
            else:
                postfixExpr = infixToPostfix(line)
                result = postfixEval(postfixExpr)
                new_line = str(result)
                write_in_file(new_line)

        else:

            if check_error(line):
                print('Error!!')
                break

            if line.count('=') > 1:
                print('Error!!')
                break

            line = line[:-1]
            var, expression = tuple(line.split('='))
            postfixExpr = infixToPostfix(expression)
            result = postfixEval(postfixExpr)
            new_line = var + '=' + str(int(result))
            # print(new_line)
            write_in_file(new_line)
