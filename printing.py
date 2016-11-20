from reports import *


def print_functions():

    print(count_games(data_file))
    print(decide(data_file, 2000))
    print(get_latest(data_file))
    print(count_by_genre(data_file, "RPG"))
    print(get_line_number_by_title(data_file, "Counter-Strike"))
    print(get_genres(data_file))

print_functions()
