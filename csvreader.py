import csv


def editrow(filename):
    with open(filename, "rb") as csvfile:
        with open("new_" + filename, "w") as csvnew:
          reader1 = csv.reader(csvfile, delimiter=',')
          writer1 = csv.writer(csvnew, delimiter=",")
          for row in reader1:
              # writer1.writerow(row)
              if "," in row[14]:
                  row[14] = row[14].replace(",",": ")
              if "," in row[8]:
                  row[8] = row[8].replace(",","+")
              writer1.writerow(row)
