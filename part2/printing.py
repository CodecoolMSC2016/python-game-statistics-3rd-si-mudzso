from reports import *
from export import *


def get_file_name():
    file_name = input("Give me input file name: ")
    return file_name


def print_input():
    while True:
        user_input = input("Give me a number(1-7): ")
        if user_input.isalpha():
            print("Wrong input")
            continue
        elif int(user_input) <= 0 or int(user_input) > 7:
            print("1-7")
            continue
        return int(user_input)


def menu_display():
    print(
        "1. What is the title of the most played game?",
        "\n2. How many copies have been sold total?",
        "\n3. What is the average selling?",
        "\n4. How many characters long is the longest title?",
        "\n5. What is the average of the release dates?",
        "\n6. What properties has a game?"
        "\n7. Export"
    )


def get_user_input():
    user_input = input("Give me a title: ")
    return str(user_input)


def print_functions(file_name):
    menu_display()
    menu_choice = print_input()
    if menu_choice == 1:
        print(get_most_played(file_name))
    elif menu_choice == 2:
        print(sum_sold(file_name))
    elif menu_choice == 3:
        print(get_selling_avg(file_name))
    elif menu_choice == 4:
        print(count_longest_title(file_name))
    elif menu_choice == 5:
        print(get_date_avg(file_name))
    elif menu_choice == 6:
        user_input = get_user_input()
        print(get_game(file_name, user_input))
    elif menu_choice == 7:
        export_file_name = input("Give me export file name: ")
        export_data(file_name, export_file_name)


def print_main():
    file_name = get_file_name()
    while True:
        print()
        print_functions(file_name)
        print()

print_main()
