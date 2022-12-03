# Simple code to alter your specific csv file
# ! Add the file you want to alter into your project folder
# Dont change the functions unless you know what you are doing
# Use the global variables to make changes 

import csv

input_file_name = "Course_info.csv"  # file to read data from
output_file_name = "test.csv"  # file to output altered version into
query_limiter = 500000  # number of rows to alter
target_row = 10  # target row to alter
value_to_replace_with = "Null"  # value to alter with


def writer(f, r):
    with open(output_file_name, 'w', encoding='UTF-8') as fs:
        w = csv.writer(fs)
        w.writerow(f)
        w.writerows(r)


def main():
    fields = []
    rows = []
    with open(input_file_name, "r", encoding='UTF-8') as fs:
        reader = csv.reader(fs)
        print(reader)
        fields = next(reader)

        for row in reader:
            rows.append(row)

        if (query_limiter > len(rows)):
            print("Query Limiter Value Is Too High")
            return ()

        for index in range(0, query_limiter):
            if (index % 2 == 0):
                rows[index][target_row] = value_to_replace_with
        writer(fields, rows)


main()
