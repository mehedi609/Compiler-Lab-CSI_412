class Entry:
    def __init__(self, hash_key, name, data_type):
        self.hash_key = hash_key
        self.name = name
        self.data_type = data_type


symbol_table = []


# check if the symbol table is empty or not
def is_empty():
    if len(symbol_table) > 0:
        return False

    return True

# num1, Integer  --> 44


# check the uesr_input is comma separated or not
def is_comma_separated(my_string):
    for chacter in my_string:
        if chacter == ',':
            return True
    return False


# to find the existing name in the symbol table
def is_match_found(name):
    index = -1
    if len(symbol_table) > 0:
        for index, element in enumerate(symbol_table):
            if name == element.name:
                return True, index
        return False, index

    return False, index


# Get the value value for the symbol table using the provided name
def get_hash_key(name):
    ascii_value = 0
    for character in name:
        ascii_value += ord(character)
    return ascii_value % 53


# Insert new Data in the symbol table
def insert(my_input):
    if is_comma_separated(my_input):
        my_input = my_input.split(',')
        name = my_input[0].strip()
        data_type = my_input[1].strip()
        hash_key = get_hash_key(name)

        # if is_empty():
        #     symbol_table.append(Entry(hash_key, name, data_type))
        #     return "Insert Successful"

        if len(symbol_table) > 54:
            return "Symtem table reached it's max limit"

        match_found, index = is_match_found(name)
        if not match_found:
            symbol_table.append(Entry(hash_key, name, data_type))
            return "Insert Successful"

        return "Sorry! Name alredy exits. Enter an unique name."

    return "Sorry! You didn't enter comma separated value."


# Search provided name in the symbol table
def search(my_input):
    match_found, index = is_match_found(my_input)

    if match_found:
        return f'Match found. Hash key is => {symbol_table[index].hash_key} and Data Type is => {symbol_table[index].data_type}'

    return 'Sorry, No Match!! Name not Found'


# Delete from the symbol table
def delete(my_input):
    match_found, index = is_match_found(my_input)
    if match_found:
        del symbol_table[index]
        return 'Delete successful'

    return 'Name not found!! No data is Deleted'


# Display the symbol talbe
def show():
    for entry in symbol_table:
        print(f"Hash Key is: {entry.hash_key} --> Name: {entry.name}  --&&--  Data Type: {entry.data_type}")


# Update an exsiting data in the symbol table
def update(my_input):
    match_found, index = is_match_found(my_input)

    if match_found:
        data_type = input('Enter new data type: ')
        if symbol_table[index].data_type == data_type:
            return 'Sorry you enter same data type. Nothing to change'

        symbol_table[index].data_type = data_type
        return 'Update successful'

    return 'Name not found!!'


while True:
    print('Enter 1 for Insert')
    print('Enter 2 for Search')
    print('Enter 3 for Delete')
    print('Enter 4 for Show')
    print('Enter 5 for Update')
    print('Enter 6 for Exit')
    user_choice = input('Enter your choice from the list: ')

    if user_choice == '1':
        user_input = input('Please insert data with comma separeted--> ')
        print(insert(user_input))
        print('')

    elif user_choice == '2':
        if is_empty():
            print('Symble table is empty! Insert data.')
        else:
            user_input = input('Please insert existing name--> ')
            print(search(user_input))
        print('')

    elif user_choice == '3':
        if is_empty():
            print('Symble table is empty! Insert data.')
        else:
            user_input = input('Please insert existing name--> ')
            print(delete(user_input))
        print('')

    elif user_choice == '4':
        if is_empty():
            print('Symble table is empty! Insert data.')
        else:
            show()
        print('')

    elif user_choice == '5':
        if is_empty():
            print('Symble table is empty! Insert data.')
        else:
            user_input = input('Please insert existing name--> ')
            print(update(user_input))
        print('')

    elif user_choice == '6':
        print('Thank you. You exit from the program')
        break
    else:
        print('You enter a wrong choice. Try again.')
        print('')
