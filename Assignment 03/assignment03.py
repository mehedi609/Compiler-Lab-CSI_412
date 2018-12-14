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


with open('input.txt') as rf:
    for line in rf:
        line = line.strip()
        if check_error(line.strip('\n')):
            print('Error!!')
            break

        with open('output.txt', 'a') as af:
            af.write(line)
