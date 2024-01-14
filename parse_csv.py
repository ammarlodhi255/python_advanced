# Reading and Writing to Comma Seperated File (CSV)

import csv

with open('./Miscellaneous/names.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    with open('./Miscellaneous/new_names.csv', 'w') as w_csv_file:
        csv_writer = csv.writer(w_csv_file, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)


# with open('./Miscellaneous/new_names.csv', 'r') as file:
#     csv_reader = csv.reader(file, delimiter='\t')
#     for line in csv_reader:
#         print(line)

with open('./Miscellaneous/names.csv', 'r') as rf:
    dict_reader = csv.DictReader(rf)    

    # for line in dict_reader:
    #     print(line['email'])

    with open('./Miscellaneous/only_names.csv', 'w') as wf:
        dict_writer = csv.DictWriter(wf, fieldnames=['first_name', 'last_name'], delimiter='\t')

        dict_writer.writeheader()

        for line in dict_reader:
            del line['email']
            dict_writer.writerow(line)