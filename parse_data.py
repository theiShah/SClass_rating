import csv
import sys
import os
import numpy as np

def read_datastruct(filename):
    dict = {'4':5,'3.7':6,'3.3':7,'3':8,'2.7':9,'2.3':10,'2':11,'1.7':12,'1.3':13,'1':14,'0.7':15,'0':16,'Pass':17,'Not Pass':18}
    with open(filename, "rt") as csvfile:
        reader1 = csv.reader(csvfile, delimiter=',')
        header = next(reader1)
        class_list = []
        for row in reader1:
            if (class_list.count(row[4]) == 0):
                class_list.append(row[4])

        reader2 = csv.reader(csvfile, delimiter=',')
        writer1 = csv.writer(csvfile, delimiter=',')
        header = next(reader2)
        curr_class = next(reader2)
        class_counter = 0
        new_row = []
        new_row[0] = header[4]
        new_row.append(header[2])
        new_row.append(header[3])
        new_row.append(header[6])
        new_row.append('Total Enrollment')
        for i in range (5, 19):
            new_row.append(dict.keys()[dict.values().index(i)])
        writer1.writerow(new_row)
        new_row = [None] * 19
        for row in reader2:
            if (curr_class[4] == class_list[class_counter]):
                new_row[dict[curr_class[2]]] = row[0]
                new_row[0] = row[] 







if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    print("Not enough arguments")
    sys.exit(0)

read_datastruct(filename)
