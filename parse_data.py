import csv
import sys
import os
import numpy as np
import sqlite3

def read_datastruct(filename):
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    cur.execute("CREATE TABLE t (col1, col2);") # use your column names here

    with open(filename,'rb') as fin: # `with` statement available in 2.5+
        # csv.DictReader uses first line in file for column headings by default
        dr = csv.DictReader(fin) # comma is default delimiter
        to_db = [(i['col1'], i['col2']) for i in dr]

    cur.executemany("INSERT INTO t (col1, col2) VALUES (?, ?);", to_db)
    con.commit()
    con.close()
