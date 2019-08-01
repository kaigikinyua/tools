import time
import os
print("<-----------Should we light up the sky,--------------->")
print("|===================== Commander =====================|\n\n")
cwd=os.getcwd()
time.sleep(3)
os.chdir('./DataFiles')
files=os.listdir()
for f in files:
	print(f)
	time.sleep(1)
filename=input("\n>")
x=open(filename,'r')
data=x.readlines()
x.close()
pline="";
for line in data:
	for c in line:
		pline+=c
		print(pline,end="\r")
		time.sleep(0.01)
	pline="";
