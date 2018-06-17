
import csv

def read_csv_avg(path):
	with open(path, newline='') as csvfile:
		datas = csv.reader(csvfile, delimiter=',')
		for data in datas:
				rowsum=0
				for i in range (len(data)):
					rowsum+=int (data[i])
				print('average = ', rowsum/len(data))
	return	
		
def main():
	path = input('Please input path of data (.csv):')
	datas = read_csv_avg(path)
	return
	
main()