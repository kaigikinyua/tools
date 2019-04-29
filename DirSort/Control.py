from Files import *
import os
class Control:
	def __init__(self):
		cwd=os.getcwd()
		f=FileActions()
		x=f.moveFile(cwd+"/todos","/home/antony/Desktop")
		if x != True:
			print (x)
		else:
			print("Moved "+cwd+"/todos to /home/antony/Desktop") 
c=Control()