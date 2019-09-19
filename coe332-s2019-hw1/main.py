from hw1.hw1 import read_data, dates, paginate

if __name__ == "__main__":
	data = read_data()
	print(data)
	print(dates(data))
	print(dates(data, start=1982))
	print(dates(data, end=1981))
	print(dates(data, start=1981, end=1983))
	print(paginate(data))
	print(paginate(data, offset=1))
	print(paginate(data, limit=3))
	print(paginate(data, offset=1, limit=2))
