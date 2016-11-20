def import_input_file(filename="game_stat.txt"):
    data_file = []
    with open(filename, "r")as import_file:
        for line in import_file.readlines():
            my_list = []
            line = line.strip("\n")
            for word in line.split("\t"):
                if word.isdigit():
                    my_list.append(int(word))
                else:
                    my_list.append(word)
            data_file.append(my_list)

    return data_file

data_file = import_input_file()


def count_games(file_name):
    return len(file_name)


def decide(file_name, year):
    for game_counter in range(len(file_name)):
        if file_name[game_counter][2] == year:
            return True
    return False


def get_latest(file_name):
    max = 0
    for game_counter in range(len(file_name)):
        if file_name[game_counter][2] > max:
            max = file_name[game_counter][2]
            position = game_counter
    return file_name[position][0]


def count_by_genre(file_name, genre):
    counter = 0
    for game_counter in range(len(file_name)):
        if file_name[game_counter][3] == genre:
            counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    checker = False
    for game_counter in range(len(file_name)):
        if file_name[game_counter][0] == title:
            checker = True
            position = game_counter + 1
    if checker:
        return position
    else:
        raise ValueError("Wrong input")


def get_genres(file_name):
    my_list = []
    for game_counter in range(len(file_name)):
        my_list.append(file_name[game_counter][3])
    my_list = sorted(set(my_list))
    return list(my_list)


def data_for_export():
    my_list = []
    my_list.append(count_games(data_file))
    my_list.append(decide(data_file, 2000))
    my_list.append(get_latest(data_file))
    my_list.append(count_by_genre(data_file, "RPG"))
    my_list.append(get_line_number_by_title(data_file, "Counter-Strike"))
    my_list.append(get_genres(data_file))
    return str(my_list)
