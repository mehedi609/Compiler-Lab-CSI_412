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
    if expression.count('(') != expression.count(')'):
        return True
    formatted_exp = expression[:-1]
    print(formatted_exp)
    for i, cha in enumerate(formatted_exp):
        if cha in '+-*/':
            if sub_error(i, formatted_exp):
                return True
        if cha is '(':
            if sub_error(i, formatted_exp):
                return True
    return False


print(check_error('100;'))
