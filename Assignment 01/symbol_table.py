# hash_key  name      data_type
# 44  ----> var_name  Integer


class Entry:
    def __init__(self, hash_key, name, data_type):
        self.hash_key = hash_key
        self.name = name
        self.data_type = data_type


symbol_table = []


def is_comma_separated(my_input):
    for character in my_input:
        if character == ',':
            return True

    return False


def get_hash_key(name):
    ascii_value = 0
    for cha in name:
        ascii_value += ord(cha)
    return ascii_value % 53


def is_match_found(name):
    index = -1
    if len(symbol_table) > 0:
        for index, element in enumerate(symbol_table):
            if element.name == name:
                return True, index
        return False, index

    return False, index


# Insert new Data in the Symbol table
# mehedi, String
# int x, x --> invalid
def insert(my_input):
    if is_comma_separated(my_input):
        user_input = my_input.split(',')
        # user_input = ['mehedi', 'String']
        name = user_input[0].strip()
        data_type = user_input[1].strip()
        hash_key = get_hash_key(name)
        new_entry = Entry(hash_key, name, data_type)

        if len(symbol_table) > 54:
            return 'Symbol table is full'

        match_found, index = is_match_found(name)

        if not match_found:
            symbol_table.append(new_entry)
            return "Insert Successful"
        return "Name already exists."

    return "Sorry! You didn't enter comma separated value."


# Display the Symbol Talbe
def show():
    for entry in symbol_table:
        print(f"Hash Key is: {entry.hash_key} --> Name: {entry.name}  --&&--  Data Type: {entry.data_type}")


def search(name):
    match_found, index = is_match_found(name)

    if match_found:
        return f"Match found. Hash Key is -> {symbol_table[index].hash_key} and Data Type -> {symbol_table[index].data_type}"

    return 'No Match. Name not found.'


def update(name):
    match_found, index = is_match_found(name)

    if match_found:
        data_type = input('Enter new data type to update: ')
        if symbol_table[index].data_type == data_type:
            return "You entered same data type. Nothing to Update"

        symbol_table[index].data_type = data_type
        return 'Update successful'

    return 'No Match. Name not found.'


def delete(name):
    match_found, index = is_match_found(name)

    if match_found:
        del symbol_table[index]
        return 'Delete Successful'

    return 'No Match. Name not found.'


while True:
    print("Enter 1 for Insert")
    print("Enter 2 for Show")
    print("Enter 3 for Search")
    print("Enter 4 for Update")
    print("Enter 5 for Delete")
    print("Enter 6 for Exit")

    user_choice = input('Enter your choice from the list: ')

    if user_choice == '1':
        user_data = input('Please insert data with comma separeted: ')
        print(insert(user_data))
        print('')

    elif user_choice == '2':
        if len(symbol_table) > 0:
            show()
            print('')
        else:
            print('Symbol table is empty. Please Insert data.')
            print('')

    elif user_choice == '3':
        if len(symbol_table) > 0:
            user_data = input('Enter existing name: ')
            print(search(user_data))
            print('')
        else:
            print('Symbol table is empty. Please Insert data.')

    elif user_choice == '4':
        if len(symbol_table) > 0:
            user_data = input('Enter existing name: ')
            print(update(user_data))
            print('')
        else:
            print('Symbol table is empty. Please Insert data.')
            print('')

    elif user_choice == '5':
        if len(symbol_table) > 0:
            user_data = input('Enter existing name: ')
            print(delete(user_data))
            print('')
        else:
            print('Symbol table is empty. Please Insert data.')
            print('')

    elif user_choice == '6':
        break

    else:
        print('You entered wrong choice. Try again.')
        print('')


























