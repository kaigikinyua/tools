import os
from Files import *
import json
import random
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

	def mine(self,filepath):
		x=open(filepath,'r')
		files=x.readlines()
		x.close()
		for file in files:
			words=file.split(' ')
			s=open('./Analysis/WordMine','a')
			for word in words:
				if word!="\n":
					w=word.split('.')
					word=w[0]
					s.write(word+"\n")
			s.close()
		d=open('./Analysis/WordMine','r')
		data=d.readlines()
		d.close()
		self.recurringWords(data)
	
	def recurringWords(self,wordlist):
		i=0
		wC=0
		recc_w={"words":[],"count":[]}
		for word in wordlist:
			if wordlist[i]=="":
				del wordlist[i]
			else:
				recc_w["words"]+=[{"word":word,"count":0}]
				wC+=1
			j=0
			for j in range(len(wordlist)):
				if(j>i):
					if word.lower()==wordlist[j].lower():
						wordlist[j]=""
				j+=1
			i+=1
			animation="|"*round(round((i/len(wordlist))*100)/10)
			print(str(round((i/len(wordlist))*100))+'% done!!'+animation,end='\r')
		d=open('./Analysis/WordRefine','w')
		for word in wordlist:
			if word!="":
				d.write(word)
		d.close()
a=AnalyzeDir()
a.mine('./DataFiles/youtube')


