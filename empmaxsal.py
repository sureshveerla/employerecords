f=None
import csv
try:
	f=open("emprec.txt","r")
	data=csv.reader(f)
	emprecs=list(data)
	big=0
	name=""
	for rec in emprecs:
		if(big<int(rec[2])):
			big=int(rec[2])
			name=rec[1]
	print(name,"Has Got Max Salary : ",big)
except:
	print("Invalid File Name")
finally:
	if f:
		f.close()


