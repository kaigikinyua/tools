import os
import json
import shutil
class FileActions:
	#contain most of the creating, reading actions on files
	#creating a file and reading one
	def appendtoFile(self,filename,data):
		try:
			f=open(filename,"r")
			d=f.readlines()
			f.close()
			f=open(filename,"w")
			f.write(d[0]+"\n"+data)
			f.close()
		except:
			print("Error Appending To File")
			return "Error Appending To file"

	#create file and write to file	
	def createFile(self,filename,action,data):
		action=action.lower()
		if action=="w":
			try:
				f.open(filename,"w")
				f.write(data)
				f.close()
				return True
			except:
				return "Failed to write to file"+filename
		elif action=="a":
			print ("appending still under Construction")
			return True
		else:
			return "Unkown File Operation "+action+" can only w/a"
	#move a file from filepath to destination	
	def moveFile(self,filepath,destination):
		try: 
			shutil.copy(filepath,destination)
			try:
				os.remove(filepath)
				return True
			except:
				return "Failed to delete file in the original folder"
		except:
			return "Failed to Copy File"
	#write to json
	def jsonWrite(self,filename,data):
		try:
			with open(filename,"w") as f:
				json.dump(data,f)
		except:
			print("Failed to write to .json File")
			return False
	#read from json
	def jsonRead(self,filename):
		try:
			with open(filename,"r") as f:
				data=json.load(f)
				return data
		except:
			print("Failed to Read json file")
			return False

	def extension(self,filename):
		try:
			ext=filename.split(".")
			return ext[len(ext)-1]
		except:
			return "no extension"
	#load settings from settings.json
