import os
import shutil
class FileActions:
	#contain most of the creating, reading actions on files
	def simpleFile(self,filename,action):
		action=action.lower()
		if action=="c":
			try: 
				f=open(filename,"w")
				f.close()
				return True
			except:
				return "Failed to create file"+filename
		elif action=="r":
			try:
				f=open(filename,"r")
				data=f.readlines()
				f.close()
				return data
			except:
				return "Failed to read file"+filename
		else:
			return "Unkown File Operation "+action+" can only c,r"

	def complexFile(self,filename,action,data):
		action=action.lower()
		if action=="w"
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




