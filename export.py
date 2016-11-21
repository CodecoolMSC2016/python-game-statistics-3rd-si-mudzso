from reports import *


def export_data(data_file, file_name="export_file.txt"):
    with open(file_name, "w")as export_file:
        export_file.write("\n1. How many games are in the file?\n")
        export_file.write(str(count_games(data_file)))
        export_file.write("\n2. Is there a game from a given year?\n")
        user_input = input("give me a year: ")
        export_file.write(str(decide(data_file, user_input)))
        export_file.write("\n3. Which was the latest game?\n")
        export_file.write(str(get_latest(data_file)))
        export_file.write("\n4. How many games do we have by genre?\n")
        user_input = input("Give me a genre: ")
        export_file.write(str(count_by_genre(data_file, user_input)))
        export_file.write("\n5. What is the line number of the given game (by title)?\n")
        user_input = input("Give me a title: ")
        export_file.write(str(get_line_number_by_title(data_file, user_input)))
        export_file.write("\n6. What are the genres?\n")
        export_file.write(str(get_genres(data_file)))
