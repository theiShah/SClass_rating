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
    with open(directory + filename, "rt") as csvfile:
        with open(directory + "new_files/new_" + filename, "w+") as csvnew:
          reader1 = csv.reader(csvfile, delimiter=',')
          writer1 = csv.writer(csvnew, delimiter=",")
          for row in reader1:
              # writer1.writerow(row)
              if "," in row[14]:
                  row[14] = row[14].replace(",",": ")
              if "," in row[8]:
                  row[8] = row[8].replace(",","+")
              row.pop(12)
              row.pop(11)
              row.pop(10)
              row.pop(5)
              row.pop(4)
              row.pop(3)
              row.pop(2)
              row.pop(1)
              if "Satisfactory" in row[5]:
                  row[5] = row[5].replace("Satisfactory","Pass")
              if "Unsatisfactory" in row[5]:
                  row[5] = row[5].replace("Unsatisfactory","Not Pass")
              writer1.writerow(row)


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
