import csv


def read_data():
	datalist = []
	field = []
	with open("rainfall.csv") as rainfile:
		csv_reader = csv.reader(rainfile)
		for row in csv_reader:
			field.append(row[0])
			field.append(row[1])
			field.append(row[2])
			break
		for row in csv_reader:
			datalist.append({field[0]: row[0], field[1]: row[1], field[2]: row[2]})
		return datalist			

		
def dates(data, start=None, end=None):
	yearlist = []
	for x in range(0,4):
		y = data[x]['year']
		y = int(y)
		if start is None and end is None: 
			yearlist.append(data[x])
		elif start is None and end is not None:
			if y<=end:
				yearlist.append(data[x])
		elif start is not None and end is None:
			if y>=start:
				yearlist.append(data[x])
		elif start is not None and end is not None:
			if y>=start and y<=end:
				yearlist.append(data[x])	 
	return yearlist

def paginate(data, offset=None, limit=None):
	dataslice = []
	if offset is not None and limit is None:
		for x in range(offset,4):
			dataslice.append(data[x])
	elif offset is None and limit is not None:
		i = 0
		for x in range(0,4):
			if i==limit:
				break
			i += 1
			dataslice.append(data[x])
	elif offset is not None and limit is not None:
		i = 0
		for x in range(offset,4):
			if i==limit:
				break
			i += 1
			dataslice.append(data[x])	
	else:
		for x in range(0,4):
			dataslice.append(data[x])		
	return dataslice
