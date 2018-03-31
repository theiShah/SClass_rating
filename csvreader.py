import csv
import sys
import os

def editrow(directory, filename):
    with open(directory + filename, "rt") as csvfile:
        with open("new_files/new_" + filename, "w+") as csvnew:
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

for filename in os.listdir(directory):
    if filename.endswith(".csv"): 
        editrow(directory, filename)
        continue
    else:
        continue
