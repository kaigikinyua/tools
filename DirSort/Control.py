from Files import *
import os
class Control:
	"""def __init__(self):
		cwd=os.getcwd()
		f=FileActions()
		x=f.moveFile(cwd+"/todos","/home/antony/Desktop")
		if x != True:
			print (x)
		else:
			print("Moved "+cwd+"/todos to /home/antony/Desktop")
	"""
	def extension(self,filename):
		try:
			ext=filename.split(".")
			return ext[1].lower()
		except:
			return "no extension"
c=Control()
x=c.extension("KINYUA.ANTONY.KAIGI")
print(x)