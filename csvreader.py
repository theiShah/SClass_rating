import csv
import sys
import os
import numpy as np

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
              writer1.writerow(row)


if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    print("Not enough arguments")
    sys.exit(0)

all_data = []

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("Working on " + filename)
        editrow(directory, filename)
        all_data.append(read_datafile(directory + "/new_files/new_" + filename))
        continue
    else:
        continue
