f=None
import csv
try:
	f=open("emprec.txt","r")
	data=csv.reader(f)
	emprecs=list(data)
	for rec in emprecs:
		if(rec[4]=='10002'and rec[1].startswith('s')and rec[3]=='M'):
			print(rec)
except:
	print("Invalid File Name")
finally:
	if f:
		f.close()


