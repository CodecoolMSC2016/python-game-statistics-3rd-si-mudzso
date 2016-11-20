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
        "1. How many games are in the file?",
        "\n2. Is there a game from a given year?",
        "\n3. Which was the latest game?",
        "\n4. How many games do we have by genre?",
        "\n5. What is the line number of the given game (by title)?",
        "\n6. What are the genres?"
    )


def get_user_input_str():
    user_input = input("Give me a text: ")
    return str(user_input)


def get_user_input_int():
    user_input = input("give me a number: ")
    return int(user_input)


def print_functions():

    menu_display()
    menu_choice = print_input()
    if menu_choice == 1:
        print(count_games(data_file))
    elif menu_choice == 2:
        int_user_input = get_user_input_int()
        print(decide(data_file, int_user_input))
    elif menu_choice == 3:
        print(get_latest(data_file))
    elif menu_choice == 4:
        str_user_input = get_user_input_str()
        print(count_by_genre(data_file, str_user_input))
    elif menu_choice == 5:
        str_user_input = get_user_input_str()
        print(get_line_number_by_title(data_file, get_user_input_str))
    elif menu_choice == 6:
        print(get_genres(data_file))


def print_main():
    while True:
        print()
        print_functions()
        print()

print_main()



