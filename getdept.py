import csv
import sys
import os

depts = []

if len(sys.argv) > 1:
    directory = sys.argv[1]
else:
    print("Not enough arguments")
    sys.exit(0)

def getdept(directory, filename):
    try:
        with open(directory + filename, "rt") as csvfile:
          reader1 = csv.reader(csvfile, delimiter=',')
          header = next(reader1)
          for row in reader1:
              if row[0] not in depts:
                  depts.append(row[0])
    except:
        pass


for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("Working on " + filename)
        getdept(directory, filename)
        continue
    else:
        continue

with open('departments.txt', "w+") as file:
    depts = sorted(depts)
    for i in range(0, len(depts)):
        file.write(depts[i])
        file.write("\n")
        print depts[i]
