import sqlite3

conn = sqlite3.connect('diagnosis.sqlite')
cur = conn.cursor()


input_data = input().strip().split(',')
result = dict()

for x in range(len(input_data)):
	data = input_data[x]
	cur.execute('''
	SELECT Diseases.name FROM Diseases JOIN Member JOIN Symptoms 
	ON Diseases.id = Member.user_id AND Member.course_id = Symptoms.id
	 WHERE Symptoms.name = ?''', (data, ))
	row = cur.fetchall()
	

	for item in row:
	
		if item[0] in result:
			result[item[0]] += 1
		else:
			result[item[0]] = 1

max_occurence = max(result.values())
print (*[disease for disease in result.keys() if result[disease]==max_occurence])
