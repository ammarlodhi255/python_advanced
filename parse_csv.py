# Reading and Writing to Comma Seperated File (CSV)

import csv

with open('./Miscellaneous/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('./Miscellaneous/new_names.csv', 'w') as w_csv_file:
        csv_writer = csv.writer(w_csv_file, delimiter='-')
        for line in csv_reader:
            csv_writer.writerow(line)