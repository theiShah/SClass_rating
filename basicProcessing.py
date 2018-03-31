import numpy as np
import sys

def read_datafile(file_name):
    # the skiprows keyword is for heading, but I don't know if trailing lines
    # can be specified
    data = np.genfromtxt(file_name, delimiter=',', names=True)
    #print(data.dtype.names)
    return data

if len(sys.argv) > 1:
    file_name = sys.argv[1]
else:
    print("Not enough arguments")
    sys.exit(0)

data = read_datafile(file_name)
names = data.dtype.names
