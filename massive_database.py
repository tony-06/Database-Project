import json
import sys


class Animal:
    def __init__(self, name, breed, gender, color):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.color = color

    def __str__(self):
        return f"Name: {self.name}\nBreed: {self.breed}\nGender: {self.gender}\nColor: {self.color}"


class Database:
    def __init__(self, filename):
        self.filename = filename
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

    def get_animals(self):
        return self.animals

    def get_last_animal(self):
        if self.animals:
            return self.animals[-1]
        else:
            return None

    def save_to_file(self):
        with open(self.filename, 'w') as f:
            animal_list = []
            for animal in self.animals:
                animal_dict = {
                    "name": animal.name,
                    "breed": animal.breed,
                    "gender": animal.gender,
                    "color": animal.color
                }
                animal_list.append(animal_dict)
            json.dump(animal_list, f)


def create_menu():
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
        'q': 'Quit'
    }
    return menu


def create_submenu():
    submenu = {
        '1': 'name',
        '2': 'breed',
        '3': 'gender',
        '4': 'color'
    }
    return submenu


def print_menu(menu):
    print('{:^60}\n{:^45}'.format('The Massive Database', '`' * 60))
    for key, value in menu.items():
        print(f"{key}. {value}")


def insert_new_animal(database):
    print("Creating a new animal...")
    name = input("Enter the animal's name: ")
    breed = input("Enter the animal's breed: ")
    gender = input("Enter the animal's gender: ")
    color = input("Enter the animal's color: ")

    # Create a new Animal object with the inputted attributes
    new_animal = Animal(name, breed, gender, color)

    # Add the new animal to the database
    database.add_animal(new_animal)

    print("Animal added to the database.")
    return database


def print_animal(database):
    last_animal = database.get_last_animal()

    if last_animal:
        print("Last animal added to the database:")
        print(last_animal)
    else:
        print("Database is empty.")
    return database


def print_all_animals(database):
    animals = database.get_animals()

    if animals:
        print("All animals in the database:")
        for animal in animals:
            print(animal)
    else:
        print("Database is empty.")
    return database


def save_database(database):
    database.save_to_file()
    print("Database saved to file:", database.filename)
    return database


def open_database():
    filename = input("Enter the filename of the database to open: ")
    with open(filename, 'r') as f:
        data = json.load(f)
    database = Database(filename)
    animals = []
    for animal_data in data:
        animal = Animal(
            name=animal_data['name'],
            breed=animal_data['breed'],
            gender=animal_data['gender'],
            color=animal_data['color']
        )
        animals.append(animal)
    database.animals = animals
    print("Database loaded from file:", filename)
    print_all_animals(database)
    return database


def create_new_database():
    filename = input("Enter a filename to save the new database: ")
    database = Database(filename)
    database.filename = filename
    print("New empty database created.")
    return database


def delete_animal(database):
    name = input("Enter the name of the animal to delete: ")
    for animal in database.animals:
        if animal.name == name:
            database.animals.remove(animal)
            print("Animal deleted from the database.")
            return
    print("Animal not found in the database.")
    return database


def search_database(database):
    attribute_dict = {1: "name", 2: "breed", 3: "gender", 4: "color"}
    print("Select an attribute to search for:")
    for key, value in attribute_dict.items():
        print(f"{key}. {value}")
    attribute_choice = int(input("Enter a number: "))
    search_string = input("Enter a search term: ")
    found_animals = []
    for animal in database.animals:
        if search_string.lower() in getattr(animal, attribute_dict[attribute_choice]).lower():
            found_animals.append(animal)
    if found_animals:
        print(f"{len(found_animals)} animal(s) found:")
        for animal in found_animals:
            print(animal)
    else:
        print("No animals found.")
    return database


def modify_animal(database):
    animal_name = input("Enter the name of the animal to modify: ")
    for animal in database.animals:
        if animal.name.lower() == animal_name.lower():
            submenu = create_submenu()
            while True:
                print("Select an attribute to modify:")
                for key, value in submenu.items():
                    print(f"{key}. {value.capitalize()}")
                choice = input("Enter your choice: ")
                if choice not in submenu:
                    print("Invalid choice. Please try again.")
                    continue
                new_value = input(f"Enter new {submenu[choice]}: ")
                setattr(animal, submenu[choice].lower(), new_value)
                print(f"{submenu[choice].capitalize()} has been updated to {new_value}.")
                break
            return
    print(f"No animal with the name {animal_name} was found in the database.")


def quit_program(database):
    # Save the database to file before quitting
    save_database(database)
    print("Exiting program. Goodbye!")
    sys.exit(0)


def get_user_input(menu, database):
    # Prompt the user for input
    user_input = input("Please select an option: ")

    # Check if the input is a valid menu option
    if user_input in menu.keys():
        # Process the user's choice
        if user_input == '1':
            create_new_database()
        elif user_input == '2':
            print_animal(database)
        elif user_input == '3':
            print_all_animals(database)
        elif user_input == '4':
            save_database(database)
        elif user_input == '5':
            open_database()
        elif user_input == '6':
            insert_new_animal(database)
        elif user_input == '7':
            delete_animal(database)
        elif user_input == '8':
            search_database(database)
        elif user_input == '9':
            modify_animal(database)
        elif user_input == 'q':
            quit_program(database)

        # Return the user's choice
        return database
    else:
        print("Invalid input. Please select a valid option.")


def main():
    menu = create_menu()
    user_database = Database("user_db")
    while True:
        print_menu(menu)
        user_database = get_user_input(menu, user_database)


if __name__ == "__main__":
    main()
