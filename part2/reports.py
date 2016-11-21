import math


def get_most_played(file_name):
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

    max = 0
    for game_counter in range(len(data_file)):
        if float(data_file[game_counter][1]) > max:
            max = data_file[game_counter][1]
            position = game_counter
    return data_file[position][0]


def sum_sold(file_name):
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
    sum = 0
    for game_counter in range(len(data_file)):
        my_list_2.append(data_file[game_counter][1])
        sum += float(my_list_2[game_counter])
    return sum


def get_selling_avg(file_name):
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
    sum = 0
    for game_counter in range(len(data_file)):
        my_list_2.append(data_file[game_counter][1])
        sum += float(my_list_2[game_counter])
        position = game_counter + 1
    return sum / position


def count_longest_title(file_name):
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

    max = 0
    for game_counter in range(len(data_file)):
        if len(data_file[game_counter][0]) > max:
            max = len(data_file[game_counter][0])
            position = game_counter
    return len(data_file[position][0])


def get_date_avg(file_name):
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
    sum = 0
    for game_counter in range(len(data_file)):
        my_list_2.append(data_file[game_counter][2])
        sum += float(my_list_2[game_counter])
        position = game_counter + 1
    return round(sum / position)


def get_game(file_name, title):
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

    checker = False
    for game_counter in range(len(data_file)):
        if data_file[game_counter][0] == title:
            checker = True
            position = game_counter
    if checker:
        data_file[position][1] = float(data_file[position][1])
        return data_file[position]
    else:
        raise ValueError("Wrong input")
