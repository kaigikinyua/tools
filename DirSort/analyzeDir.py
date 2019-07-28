import os
from Files import *
import json
class AnalyzeDir:
	def getdir(self):
		directory=input("Enter a directory to analyze\n")
		self.dircontent(directory)
	def dircontent(self,dir):
		cwd=os.getcwd()
		if(os.path.isfile):
			os.chdir(dir)
			dircontent=os.listdir()
			os.chdir(cwd)
			dirFile=dir.split('/')
			filename=dirFile[len(dirFile)-1]
			logname='./DataFiles/'+filename
			f=open(logname,'w')
			for c in dircontent:
				writedata=c+"\n"
				f.write(writedata)
			f.close()
			print("Directory content has been saved to "+logname)
			self.analysis(dircontent,filename)
		else:
			print(dir+" is not a directory")
	def analysis(self,directorycontent,dirname):
		F=FileActions()
		a=open('./Analysis/'+dirname+'.json','w')
		a.close()
		#a=open('./Analysis/'+dirname+'.json','a')
		extensions=[]
		extensionscontent=[]
		for file in directorycontent:
			e=F.extension(file)
			extensions+=[e]
			extensionscontent+=[e]
		i=0
		distinctextensions=[]
		for ext in extensions:
			for j in range(len(extensions)):
				if(j>i):
					if extensions[j]==ext:
						extensions[j]=""
			if(extensions[i]!=""):
				distinctextensions+=[extensions[i]]			
			i+=1
		print("Number of files in "+dirname+" is "+str(len(extensions)))
		number=[]
		for ext in distinctextensions:	
			number+=[self.countExtensions(ext,extensionscontent)]

		print(distinctextensions)
		print(number)
		analysis={"overalanalysis":[],"extensions_analysis":[]}
		i=0
		extpercentage=[]
		for ext in distinctextensions:
			analysis["extensions_analysis"]+=[{"ext":ext,"number":number[i]}]
			extpercentage+=[self.calculatePercentage(number[i],len(extensionscontent))]
			i+=1

		sortedlist=self.sort(extpercentage)
		print(sortedlist)
		analysis["overalanalysis"]=[{"percentage":sortedlist[0]} ]
		
		F.jsonWrite('./Analysis/'+dirname+".json",analysis)
	def countExtensions(self,ext,extlist):
		number=0
		for e in extlist:
			if e==ext:
				number+=1
		return number
	def calculatePercentage(self,number,total):
		percentage=(number/total)*100
		return percentage
	def sort(self,datalist):
		for i in range(len(datalist)-1):
			if(datalist[i]<datalist[i+1]):
				holder=datalist[i]
				datalist[i]=datalist[i+1]
				datalist[i+1]=holder
		return datalist
a=AnalyzeDir()
a.getdir()


