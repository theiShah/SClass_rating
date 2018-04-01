import csv
import sys
import os
import numpy as np
# from parse_data import read_datastruct

def read_datafile(file_name):
    # the skiprows keyword is for heading, but I don't know if trailing lines
    # can be specified
    data = np.genfromtxt(file_name, delimiter=",", names=True)
    #print(data.dtype.names)
    return data


def editrow(directory, filename):
    try:
        with open(directory + filename, "rt") as csvfile:
            with open(directory + "new_files/new_" + filename, "w+") as csvnew:
              reader1 = csv.reader(csvfile, delimiter=',')
              writer1 = csv.writer(csvnew, delimiter=",")
              i = 1
              for row in reader1:
                  if (row[12] != 'NR'):
                      if (row[2] == '1') or row[2] == 'SESSION':
                          for i in range(0,8):
                              row.pop(44-i)
                          for i in range(12, 26):
                              row.pop(44-i)
                          row.pop(14)
                          row.pop(7)
                          row.pop(5)
                          row.pop(3)
                          row.pop(2)
                          row.pop(1)
                          row.pop(0)
                          row.pop(13)
                          row.pop(13)
                          row.pop(14)

                          writer1.writerow(row)
    except:
        pass


if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    print("Not enough arguments")
    sys.exit(0)

all_data = []
all_filenames = []

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("Working on " + filename)
        editrow(directory, filename)
        # read_datastruct(directory + "/new_files/new_" + filename)
        # all_data.append(read_datafile(directory + "/new_files/new_" + filename))
        # all_filenames.append(filename)
        continue
    else:
        continue

# for struct in all_data:
#     read_datastruct(struct)
