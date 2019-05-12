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
	def move(self):
		cwd=os.getcwd()
		directory=input("Enter the directory you would like to sort\n")
		F=FileActions()
		settings=F.jsonRead("settings.json")
		if(settings!=False):
			print("Here are your current settings for moving the files\n\n")
			for s in settings["settings"]:
				print(s["ext"]+"\t"+s["dir"])
			ans=input("Would you like to use these settings?\t[y/n]\n")
	#extract extensions
c=Control()
x=c.move()
