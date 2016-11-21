

def count_games(file_name):
    data_file = []
    with open(file_name, "r")as import_file:
        for line in import_file.readlines():
            my_list = []
            line = line.strip("\n")
            for word in line.split("\t"):
                if word.isdigit():
                    my_list.append(float(word))
                else:
                    my_list.append(word)
            data_file.append(my_list)

    return len(data_file)


def decide(file_name, year):
    data_file = []
    with open(file_name, "r")as import_file:
        for line in import_file.readlines():
            my_list = []
            line = line.strip("\n")
            for word in line.split("\t"):
                if word.isdigit():
                    my_list.append(float(word))
                else:
                    my_list.append(word)
            data_file.append(my_list)

    for game_counter in range(len(data_file)):
        if data_file[game_counter][2] == year:
            return True
    return False


def get_latest(file_name):
    data_file = []
    with open(file_name, "r")as import_file:
        for line in import_file.readlines():
            my_list = []
            line = line.strip("\n")
            for word in line.split("\t"):
                if word.isdigit():
                    my_list.append(float(word))
                else:
                    my_list.append(word)
            data_file.append(my_list)

    max = 0
    for game_counter in range(len(data_file)):
        if data_file[game_counter][2] > max:
            max = data_file[game_counter][2]
            position = game_counter
    return data_file[position][0]


def count_by_genre(file_name, genre):
    data_file = []
    with open(file_name, "r")as import_file:
        for line in import_file.readlines():
            my_list = []
            line = line.strip("\n")
            for word in line.split("\t"):
                if word.isdigit():
                    my_list.append(float(word))
                else:
                    my_list.append(word)
            data_file.append(my_list)

    counter = 0
    for game_counter in range(len(data_file)):
        if data_file[game_counter][3] == genre:
            counter += 1
    return counter


def get_line_number_by_title(file_name, title):
    data_file = []
    with open(file_name, "r")as import_file:
        for line in import_file.readlines():
            my_list = []
            line = line.strip("\n")
            for word in line.split("\t"):
                if word.isdigit():
                    my_list.append(float(word))
                else:
                    my_list.append(word)
            data_file.append(my_list)

    checker = False
    for game_counter in range(len(data_file)):
        if data_file[game_counter][0] == title:
            checker = True
            position = game_counter + 1
    if checker:
        return position
    else:
        raise ValueError("Wrong input")


def get_genres(file_name):
    data_file = []
    with open(file_name, "r")as import_file:
        for line in import_file.readlines():
            my_list = []
            line = line.strip("\n")
            for word in line.split("\t"):
                if word.isdigit():
                    my_list.append(int(word))
                else:
                    my_list.append(str(word))
            data_file.append(my_list)

    my_list_2 = []
    for game_counter in range(len(data_file)):
        my_list.append(data_file[game_counter][3])
    my_list_2 = sorted(set(my_list_2))
    return list(my_list_2)
