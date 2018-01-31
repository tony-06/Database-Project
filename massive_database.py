def menu():
    print('{:^60}\n{:^45}'.format('The Massive Database', '`' * 60))
    menu = {
        '1': 'Create New',
        '2': 'Print',
        '3': 'Print All',
        '4': 'Save',
        '5': 'Open',
        '6': 'Insert New',
        '7': 'Delete',
        '8': 'Search',
        '9': 'Modify',
        'Q': 'Quit'}
    while True:
        for key in menu.keys():
            print(key, menu[key])
        user_selection = input('Select an option:\n')
        if user_selection in menu.keys():
            if user_selection == '1':
                user_list = animal_list()
            elif user_selection == '2':
                print_animal(user_list[-1])
            elif user_selection == '3':
                for i in user_list:
                    print_animal(i)
            elif user_selection == '4':
                save_list = input('Enter a filename:\n')
                new_file = open(save_list, 'w')
                for item in user_list:
                    file_string = str(item[0] + ', ' + item[1] + ', ' + item[2] + ', ' + item[3] + ', ')
                    new_file.write(file_string)
                new_file.close()
            elif user_selection == '5':
                user_list = []
                open_list = input('Enter a filename:\n')
                user_file = open(open_list)
                user_file = user_file.read()
                x = user_file.split(', ')
                try:
                    for i in range(len(x) - 1):
                        y = x[:4]
                        user_list.append(y)
                        x.pop(0)
                        x.pop(0)
                        x.pop(0)
                        x.pop(0)
                except:
                    pass
                user_list.pop(-1)
            elif user_selection == '6':
                user_list.append(new_animal())
            elif user_selection == '7':
                object_delete = input('Type the name of the animal you would like to remove:\n')
                x = animal_search(user_list, object_delete)
                user_list.remove(x)
            elif user_selection == '8':
                object_find = input('Search by name:\n')
                x = animal_search(user_list, object_find)
                print_animal(x)
            elif user_selection == '9':
                object_modify = input('Name of animal you would like to modify:\n')
                x = animal_search(user_list, object_modify)
                modify_animal(x)
            elif user_selection == 'Q':
                break
        else:
            print('Invalid selection')


def new_animal():
    name = input('Name?\n')
    breed = input('Breed?\n')
    gender = input('Gender?\n')
    color = input('Color?\n')
    return [name, breed, color, gender]


def animal_list():
    user_list = []
    while True:
        user_animal = new_animal()
        user_list.append(user_animal)
        add_more = input('Add another?\nY/N\n')
        if add_more == 'Y':
            continue
        elif add_more == 'N':
            break
        else:
            print('Invalid Selection')
    return user_list


def animal_search(user_list, name):
    for i in user_list:
        if i[0] == name:
            return i


def modify_animal(animal):
    attribute = input('What would you like to change?\n(name, breed, gender, color)\n')
    if attribute == 'name':
        name = input('New name?:\n')
        animal[0] = name
    elif attribute == 'breed':
        breed = input('New breed?\n')
        animal[1] = breed
    elif attribute == 'gender':
        gender = input('New gender?\n')
        animal[3] = gender
    elif attribute == 'color':
        color = input('New color?\n')
        animal[2] = color
    else:
        print('Invalid selection')


def print_animal(name):
    print('{:20}{:20}{:20}{:20}'.format(name[0], name[1], name[2], name[3]))


menu()
