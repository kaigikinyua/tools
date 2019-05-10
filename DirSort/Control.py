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
	#extract extensions
	def extension(self,filename):
		try:
			ext=filename.split(".")
			return ext[len(ext)-1]
		except:
			return "no extension"
	#load settings from settings.json
c=Control()
x=c.settings()
print(x)
