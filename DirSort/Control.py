from Files import *
import os
class Control:
	"""
	 program flow 
	 	1.Enter The Directory You would Like to Sort
	 	2.Load Settings and Display Them to the user(ask if to continue or edit or exit)
	 	3.If yes then start by sorting the files and moving them
	 	4.If edit then Edit the file settings
	 	5.Advanced Thread for moving files
	"""
	def previewSettings(self):
		cwd=os.getcwd()
		directory=input("Enter the directory you would like to sort\n")
		if(os.path.isdir(directory)):
			F=FileActions()
			settings=F.jsonRead("settings.json")
			if(settings!=False):
				print("Here are your current settings for moving the files\n\n")
				for s in settings["settings"]:
					print(s["ext"]+"\t"+s["dir"])
				ans=input("Would you like to use these settings?\t[y/n]\n")
				if ans.lower()=="y":
					#call method to sortFiles
					print ("method to move files using settings")
					f=FileActions()
					i=0;
					directoryList=os.listdir(directory)
					for i in range(len(settings["settings"])-1):
						fileExt=settings["settings"][i]["ext"]
						j=0
						for j in range(len(directoryList)-1):
							if fileExt.lower()==f.extension(directoryList[j]):
								r=f.moveFile(directory+'/'+directoryList[j],settings["settings"][i]["dir"])
								if(r!=True):
									print(r)
				else:
					c=Control()
					c.loadNewSettings()
			else:
				print(settings)
		else:
			print("Not a valid directory")
			c=Control()
			c.previewSettings()

	def loadNewSettings(self):
		print("Enter the Extension and the Directory you wolud like to place it\nenter Q! to quit")
		Settings={"settings":[]}
		ext="";q="";
		while(q!="Q!" or q!="q!"):
			extension=input("Enter the extension\n")
			directory=input("Enter the directory to place it\n")
			Settings["Settings"]+=[{"ext":extension,"dir":directory}];
			q=input("Press Q! or q! to quit")
		print(Settings["Settings"])

c=Control()
x=c.previewSettings()
