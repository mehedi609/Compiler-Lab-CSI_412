def compute(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    if operator == '-':
        return num1 - num2
    if operator == '*':
        return num1 * num2
    if operator == '/':
        return num1 / num2


user_input = '-+32+57'
numbers = list(user_input)
numbers.reverse()
print(numbers)

while True:
    for index, number in enumerate(numbers):
        if not number.isdecimal():
            operator = numbers[index]
            num1 = int(numbers[index-1])
            num2 = int(numbers[index-2])
            res = compute(num1, num2, operator)
            numbers.insert(index+1, str(res))
            del numbers[index-2:index+1]
            print(numbers)
            break
    if len(numbers) == 1:
        print(numbers[0])
        break
