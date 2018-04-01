import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='',
    db='test')
cursor = mydb.cursor()

csv_data_classes = csv.reader(file('data/new_files/new_su2015.csv'))
csv_data = csv.reader(file('data/new_files/new_su2015.csv'))
csv_data2 = csv.reader(file('data/new_files/new_su2015.csv'))

classes = dict()
dict = {'4':'num_A','3.7':'num_Am','3.3':'num_Bp','3':'num_B','2.7':'num_Bm', \
	'2.3':'num_Cp','2':'num_C','1.7':'num_Cm','1.3':'num_Dp','1':'num_D', \
	'0.7':'num_Dm','0':'num_F','Pass':'num_pass','Not Pass':'num_nopass'}

row_header = next(csv_data_classes)
for row in csv_data_classes:
	if row[3] not in classes or classes[row[3]].count(row[4]) == 0:
		#classes.append(row[4])
		if row[3] in classes: 
			classes[row[3]].append(row[4])
		else:
			classes[row[3]] = [row[4]]
		cursor.execute('INSERT INTO ratemyclass(course_number,professors,course_subject,course_name)' \
			'VALUES(%s, %s, %s, %s)', (row[4],row[1],row[3],row[6]))

row_header = next(csv_data)
for row in csv_data:
	course_num = row[4]
	num = row[0]
	col = ''
	if row[2] not in (None, ""):
		col = dict[row[2]]
	else:
		col = dict[row[5]]
	cursor.execute ("""UPDATE ratemyclass
   		SET """ + col + """ = %s
  		WHERE course_number=%s
		""", (num,course_num))



row_header = next(csv_data2)
row_first = next(csv_data2)
curr_class = row[4]
curr_subj = row[3]
total = row[0]
for row in csv_data2:
	if (curr_class == row[4] and curr_subj == row[3]):
		total += int(row[0])
	else:
		cursor.execute("""UPDATE ratemyclass
   		SET total_enrollment = %s
  		WHERE course_number=%s and course_subject=%s
		""", (total,curr_class, curr_subj))
		curr_class = row[4]
		total = int(row[0])
		curr_subj = row[3] 
    
#close the connection to the database.
mydb.commit()
cursor.close()
print "Done"