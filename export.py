from reports import *
from printing import print_functions


def export_data(file_name="export_file.txt"):
    with open(file_name, "w")as export_file:
        export_file.write(data_for_export())

export_data()
