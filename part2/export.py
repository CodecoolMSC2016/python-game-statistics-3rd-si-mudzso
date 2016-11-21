from reports import *


def export_data(data_file, file_name="export_file.txt"):
    with open(file_name, "w")as export_file:
        export_file.write("\n1. What is the title of the most played game?\n")
        export_file.write(str(get_most_played(data_file)))
        export_file.write("\n2. How many copies have been sold total?\n")
        export_file.write(str(sum_sold(data_file)))
        export_file.write("\n3. What is the average selling?\n")
        export_file.write(str(get_selling_avg(data_file)))
        export_file.write("\n4. How many characters long is the longest title?\n")
        export_file.write(str(count_longest_title(data_file)))
        export_file.write("\n5. What is the average of the release dates?\n")
        export_file.write(str(get_date_avg(data_file)))
        export_file.write("\n6. What properties has a game?\n")
        user_input = input("Give me a title: ")
        export_file.write(str(get_game(data_file, user_input)))
