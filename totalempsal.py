f=None
import csv
try:
	f=open("emprec.txt","r")
	data=csv.reader(f)
	emprecs=list(data)
	sum=0
	for rec in emprecs:
		sum=sum+int(rec[2])
	print("sum of all employee salaries = ",sum)
except:
	print("Invalid File Name")
finally:
	if f:
		f.close()