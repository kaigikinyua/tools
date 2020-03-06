import os
from bolt import *
from messages import *
class Search():

    #main method
    def main(self):
        filename=input("Enter filename to search:\n")
        if(os.path.exists("./"+filename)):
            try:
                #try openning the file
                fm=FileManage(filename)
                x=fm.readFile()
                if(x!=False):
                    #if the readFile method returns notFasle the file is read
                    m=Messages()
                    message=m.message("s","Reading file "+filename);
                    print (message)
                    #function for search
                    ans=input("Enter 1 for to search for exact word or \n2 for like word\n")
                    s=Search()
                    word=input("enter the word you are searching for\n>")
                    if ans==str("1"):
                        #pass the fileContent to the exactword function you would like to search for
                        s.exactWord(x,word)
                    else:
                        print ("Add * to the letters you would like to skip/dont know")
                        s.likeWord(x,word)
                else:
                    m=Messages()
                    message=m.message("f","Reading file "+filename);
                    print (message)
            except():
                m=Messages()
                message=m.message("f","Opening file "+filename);
                print (message)
        else:
            ans=input("Error 404 :(\nwould you like to create a new file? :)\ny/n\n")
            if(ans.lower()=="y"):
                b=FileManage(filename)
                if(b.writeToFile("Hello World")!=True):
                    m=Messages()
                    message=m.message("f","Opening file "+filename);
                    print (message)
                else:
                    m=Messages()
                    message=m.message("s","Writing to file "+filename);
                    print (message)

    #search engine -- vroom
    def exactWord(self,fileContent,search):
        lineNo=0
        s=Search()
        for line in fileContent:
            if s.newLineSep(line.lower())==search.lower():
                print (lineNo+1)
                break
            else:
                lineNo+=1
    #def likeWord(self):
    def likeWord(self,fileContent,word):
        #using slices
        #total word count
        searchSpace=len(fileContent)
        if word[0]=="*":
            #slice begins at 1
            line_count=1
            for myWord in fileContent:
                i=0
                for char in myWord:
                    if word[1]==char:
                        #enter a loop to check for the slice
                        word_s=[];myWord_s=[];
                        word_s+=word;myWord_s+=myWord
                        if word_s[1:len(word)]==myWord_s[i:len(word)]:
                            print(str(word_s[1:len(word)])+" matches with "+str(myWord_s[i:len(word)])+" at line "+str(line_count))
                        else:
                            print(word_s[1:len(word)])
                            print(myWord_s[i:len(word)])
                            print("\n")
                    i+=1
                line_count+=1

        elif word[len(word)-1]=="*":
            #slice ends at len(word)-1
            line_count=1
            for myWord in fileContent:
                i=0
                for char in myWord:
                    if word[0]==char:
                        word_s=[];myWord_s=[];
                        word_s+=word;myWord_s+=myWord;
                        if word_s[0:len(word)-1] == myWord_s[i:len(word)-1]:
                            print(str(word_s[0:len(word)])+" matches with "+str(myWord_s[i:len(word)])+" at line "+str(line_count))
                        else:
                            print(word_s[0:len(word)-1])
                            print(myWord_s[i:len(word)-1])
                            print("\n")
                    i+=1
                line_count+=1
        else:
            print("Please use a ' * '")
    #character support
    def newLineSep(self,word):
        w=""
        for i in range(len(word)):
            if (word[i]=="\n" or word[i]==" "):
                return w
            else:
                w+=word[i]
s=Search()
s.main()
