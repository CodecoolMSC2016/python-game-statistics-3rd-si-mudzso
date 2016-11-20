from reports import *


def print_input():
    while True:
        user_input = input("Give me a number(1-6): ")
        if user_input.isalpha():
            print("Wrong input")
            continue
        elif int(user_input) <= 0 or int(user_input) > 6:
            print("1-6")
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
    )


def get_user_input():
    user_input = input("Give me a title: ")
    return str(user_input)


def print_functions():
    menu_display()
    menu_choice = print_input()
    if menu_choice == 1:
        print(get_most_played(data_file))
    elif menu_choice == 2:
        print(sum_sold(data_file))
    elif menu_choice == 3:
        print(get_selling_avg(data_file))
    elif menu_choice == 4:
        print(count_longest_title(data_file))
    elif menu_choice == 5:
        print(get_date_avg(data_file))
    elif menu_choice == 6:
        user_input = get_user_input()
        print(get_game(data_file, user_input))


def print_main():
    while True:
        print()
        print_functions()
        print()

print_main()
