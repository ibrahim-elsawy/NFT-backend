from datetime import datetime


def calculateDate(*dateStart):
	dateNow = datetime.today()
	formDate = ["year", "month", "day", "hour", "minute"]
	for d,n  in zip(dateStart, formDate):
		diff = dateNow.__getattribute__(n) - d
		if diff ==1:
			return [diff, n]
		elif diff > 1:
			return [diff, n+'s']
		elif n=="minute" and diff==0:
			return[1, "minute"]



if __name__ == '__main__':
	print(calculateDate(2022, 4, 26, 3, 19))