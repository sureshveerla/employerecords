f=None
import csv
try:
	f=open("emprec.txt","r")
	data=csv.reader(f)
	emprecs=list(data)
	small=int(emprecs[0][2])
	name=""
	for rec in emprecs:
		if(small>int(rec[2])):
			small=int(rec[2])
			name=rec[1]
	print(name,"Has Got Min Salary : ",small)
except:
	print("Invalid File Name")
finally:
	if f:
		f.close()


