f=None
import csv
try:
	f=open("emprec.txt","r")
	data=csv.reader(f)
	emprecs=list(data)
	msum=0
	fsum=0
	for rec in emprecs:
		if(rec[3]=='M'):
			msum=msum+int(rec[2])
		else:
			fsum=fsum+int(rec[2])
	print("sum of all Male employee salaries : ",msum)
	print("sum of all Female employee salaries : ",fsum)
except:
	print("Invalid File Name")
finally:
	if f:
		f.close()


