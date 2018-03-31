import csv

def read_datafile(file_name):
	with open(file_name, "rb") as f:
	    reader = csv.reader(f, delimiter=",")
	    for i, line in enumerate(reader):
	        


if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("Not enough arguments")
    sys.exit(0)

data = read_datafile(file_name)