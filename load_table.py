import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='test')
cursor = mydb.cursor()

csv_data_classes = csv.reader(file('data/new_files/new_su2015.csv'))
csv_data = csv.reader(file('data/new_files/new_su2015.csv'))

classes = []
row_header = next(csv_data_classes)
for row in csv_data_classes:
	if classes.count(row[4]) == 0:
		classes.append(row[4])
		cursor.execute('INSERT INTO ratemyclass(course_number,professors,course_subject,course_name)' \
			'VALUES(%s, %s, %s, %s)', (row[4],row[1],row[3],row[6]))


    
#close the connection to the database.



mydb.commit()
cursor.close()
print "Done"