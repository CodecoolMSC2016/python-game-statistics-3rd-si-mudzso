import math



def import_input_file(filename="game_stat.txt"):
    data_file = []
    with open(filename, "r")as import_file:
        for line in import_file.readlines():
            my_list = []
            line = line.strip("\n")
            for word in line.split("\t"):
                if word.isdigit():
                    my_list.append(float(word))
                else:
                    my_list.append(word)
            data_file.append(my_list)

    return data_file

data_file = import_input_file()


def get_most_played(file_name):
    max = 0
    for game_counter in range(len(file_name)):
        if float(file_name[game_counter][1]) > max:
            max = file_name[game_counter][1]
            position = game_counter
    return file_name[position][0]

def sum_sold(file_name):
    my_list = []
    sum = 0
    for game_counter in range(len(file_name)):
        my_list.append(file_name[game_counter][1])
        sum += float(my_list[game_counter])
    return sum

def get_selling_avg(file_name):
    my_list = []
    sum = 0
    for game_counter in range(len(file_name)):
        my_list.append(file_name[game_counter][1])
        sum += float(my_list[game_counter])
        position = game_counter + 1
    return sum / position

def count_longest_title(file_name):
    max = 0
    for game_counter in range(len(file_name)):
        if len(file_name[game_counter][0]) > max:
            max = len(file_name[game_counter][0])
            position = game_counter
    return len(file_name[position][0])

def get_date_avg(file_name):
    my_list = []
    sum = 0
    for game_counter in range(len(file_name)):
        my_list.append(file_name[game_counter][2])
        sum += float(my_list[game_counter])
        position = game_counter + 1
    return round(sum / position)

def get_game(file_name, title):
    checker = False
    for game_counter in range(len(file_name)):
        if file_name[game_counter][0] == title:
            checker = True
            position = game_counter 
    if checker:
        return file_name[position]
    else:
        raise ValueError("Wrong input")


def data_for_export():
    my_list = []
    my_list.append(get_most_played(data_file))
    my_list.append(sum_sold(data_file))
    my_list.append(get_latest(data_file))
    my_list.append(count_by_genre(data_file, "RPG"))
    my_list.append(get_line_number_by_title(data_file, "Counter-Strike"))
    my_list.append(get_genres(data_file))
    return str(my_list)
