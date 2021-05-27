import re
class KeyWords:
    def __init__(self,datalist):
        self.datalist=datalist

    def frequentWords(self):
        foundWords=[]
        matchedKeyWords=[
            #{"word":0}
        ]
        for f in self.datalist:
            words=self.splitWords(f)
            for word in words:
                if(word.lower() in foundWords):
                    print(matchedKeyWords)
                    matchedKeyWords[{word.lower()}]+=1
                else:
                    foundWords+=[word.lower()]
                    matchedKeyWords+=[{word.lower():1}]
        print(matchedKeyWords)

    def splitWords(self,sentence):
        words=re.findall('[\w]*',sentence)
        refinedWords=[]
        for word in words:
            if(len(word)>0):
                refinedWords+=[word]
        return refinedWords

if __name__=="__main__":
    sentences=['One two three four five one two three','One quick']
    k=KeyWords(sentences)
    print(k.frequentWords())

