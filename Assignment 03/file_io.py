def split_into_var_n_expression(line):
    # mylist = line.split('=')
    var, expression = tuple(line.split('='))
    print(var)
    print(expression)


def get_value_from_output(token):
    with open('output.txt') as rf:
        for line in rf:
            line = line.strip()
            if '=' in line:
                var, value = tuple(line.split('='))
                if token == var:
                    return value

# print(get_value_from_output('a'))


# with open('input.txt') as rf:
#     for line in rf:
#         line = line.strip()[:-1]
#         if '=' in line:
#             if line.count('=') > 1:
#                 print('Error')
#                 break
#         print(line)
#         # with open('output.txt', 'a') as af:
#         #     af.write(line)

print(list('28a'))

