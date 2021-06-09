import json,re
from utils import *
class ScorePoints:
    def __init__(self,fileList):
        self.fileList=fileList

    def fileScore(self):
        keywords=None
        with open('./mykeywords.json','r') as f:
            data=json.load(f)
            keywords=data["keywords"]
        scoredFiles=[]
        for f in self.fileList:
            for category in keywords:
                matches=0
                matches_count=0
                for word in category["words"]:
                    matches=re.findall(word, f.lower())
                    c=self.countNonEmpty(matches)
                    matches_count+=c
                c=category["name"]
                filename=f
                print("File {f} has scored {d} in category {c}".format(f=f,c=c,d=matches_count))

    def countNonEmpty(self,array):
        count=0
        for item in array:
            if(len(item)>0 and item!=''):
                count+=1
        return count


if __name__=="__main__":
    f=Directory("/home/antony/Downloads/Video")
    files=f.listFiles()
    s=ScorePoints(files)
    s.fileScore()



