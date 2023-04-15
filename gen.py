import csv
import random

header = ["Time between stop A and B", "Day of the week", "Time of the day", "Late"]
data = []
# time. between A and B, day of the week, hour of the day, late?

flag = 0
for i in range(50000):
	data.append([0,0,0,0])
	data[i][0] = random.randint(1,20)
	data[i][1] = random.randint(0,6)
	data[i][2] = random.randint(7,21)
	flag = random.randint(0,5)
	if flag != 0:
		if data[i][0] < 6 and data[i][1] != 6:
			data[i][3] = 1
		else:
			data[i][3] = 0
	else:
		data[i][3] = random.randint(0,1)

filename = "data.csv"

with open(filename, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    csvwriter.writerows(data)