import string


# Check for any Special Character in String
def has_any_special_character(word):
    invalid_chars = set(string.punctuation.replace("_", ""))
    if any(char in invalid_chars for char in word):
        return True
    return False


# Regular Expression for integer number
def integer_regex(reg_exp):
    if reg_exp[0] == '0':
        return False
    if not reg_exp.isnumeric():
        return False
    return True


# Regular Expression for Variables
def variable_regex(reg_exp):
    if reg_exp[0].isnumeric():
        return f"{reg_exp}  -->  Not  Valid"
    if has_any_special_character(reg_exp):
        return f"{reg_exp}  -->  Not  Valid"
    if ' ' in reg_exp:
        return f"{reg_exp}  -->  Not  Valid"
    return f"{reg_exp}  -->  Valid"


# Regular Expression for Float Number
def float_regex(reg_exp):
    if any(cha.isalpha() for cha in reg_exp):
        return False
    if '.' not in reg_exp:
        return False
    if not len(reg_exp.split('.')[1]):
        return False
    if ' ' in reg_exp:
        return False
    return True


# Regular Expression for Exponent
def exponent_regex(reg_exp):
    if 'E' not in reg_exp:
        return f"{reg_exp}  -->  Not  Valid"
    reg_exp_list = reg_exp.split('E')
    left = reg_exp_list[0]
    right = reg_exp_list[1]
    if not len(reg_exp_list) == 2:
        return f"{reg_exp}  -->  Not  Valid"
    else:
        if not len(right) > 0:
            return f"{reg_exp}  -->  Not  Valid"
        if not float_regex(left):
            return f"{reg_exp}  -->  Not  Valid"
        if right[0] in ['+', '-']:
            if len(right[1:]) is 1 and int(right[1:]) is 0:
                return f"{reg_exp}  -->  Not  Valid"
            if not right[1:].isnumeric():
                return f"{reg_exp}  -->  Not  Valid"
        else:
            if len(right) is 1 and int(right) is 0:
                return f"{reg_exp}  -->  Not  Valid"
            if not right.isnumeric():
                return f"{reg_exp}  -->  Not  Valid"
    return f"{reg_exp}  -->  Valid"


# Regular Expression for n Character
def n_character_regex(reg_exp):
    if reg_exp[0] is not 'n':
        return f"{reg_exp}  -->  Not  Valid"
    if reg_exp[1].isdigit():
        return f"{reg_exp}  -->  Not  Valid"
    if has_any_special_character(reg_exp):
        return f"{reg_exp}  -->  Not  Valid"
    if ' ' in reg_exp:
        return f"{reg_exp}  -->  Not  Valid"
    return f"{reg_exp}  -->  Valid"


while True:
    print('Press 1 for Integer Regex')
    print('Press 2 for Variable Regex')
    print('Press 3 for Float Regex')
    print('Press 4 for Exponent Regex')
    print('Press 5 for nCharacter Regex')
    print('Press 6 for Exit')
    print('')

    user_choice = input('Enter your choice: ')

    # choose to check regex for integer number
    if user_choice == '1':
        user_input = input('Enter a valid Integer Number-->  ')
        if len(user_input):
            if user_input[0] in ['+', '-']:
                if integer_regex(user_input[1:]):
                    print(f"{user_input}  -->  Valid", end='\n\n')
                else:
                    print(f"{user_input}  -->  Not Valid", end='\n\n')
            else:
                if integer_regex(user_input):
                    print(f"{user_input}  -->  Valid", end='\n\n')
                else:
                    print(f"{user_input}  -->  Not Valid", end='\n\n')
        else:
            print('You did not enter anything', end='\n\n')

    # choose to check regex for Variables
    elif user_choice == '2':
        user_input = input('Enter a valid Variables-->  ')
        if len(user_input):
            print(variable_regex(user_input), end='\n\n')
        else:
            print('You did not enter anything', end='\n\n')

    # choose to check regex for Float Number
    elif user_choice == '3':
        user_input = input('Enter a valid Float Number-->  ')
        if len(user_input):
            if user_input[0] in ['+', '-']:
                if float_regex(user_input[1:]):
                    print(f"{user_input}  -->  Valid", end='\n\n')
                else:
                    print(f"{user_input}  -->  Not Valid", end='\n\n')
            else:
                if float_regex(user_input):
                    print(f"{user_input}  -->  Valid", end='\n\n')
                else:
                    print(f"{user_input}  -->  Not Valid", end='\n\n')
        else:
            print('You did not enter anything', end='\n\n')

    # choose to check regex for Exponent
    elif user_choice == '4':
        user_input = input('Enter a valid Exponent Number-->  ')
        if len(user_input):
            if user_input[0] in ['+', '-']:
                print(user_input[0] + exponent_regex(user_input[1:]), end='\n\n')
            else:
                print(exponent_regex(user_input), end='\n\n')
        else:
            print('You did not enter anything', end='\n\n')

    # choose to check regex for n Character
    elif user_choice == '5':
        user_input = input('Enter a valid Variables staring with n-->  ')
        if len(user_input):
            print(n_character_regex(user_input), end='\n\n')
        else:
            print('You did not enter anything', end='\n\n')

    # choose to exit from the program
    elif user_choice == '6':
        print('Thank you for using this app. Good Bye!!')
        break

    else:
        print('You entered wrong choice!!', end='\n\n')
