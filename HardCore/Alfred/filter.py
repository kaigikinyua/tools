import sqlite3

class Filter:
    def __init__(self,sentence,command):
        if command=="0":
            if self.filter(sentence)==False:
                print("Sorry, your sentence is rude")
            elif self.filter(sentence)==True:
                print("Analyzing input")
            else:
                print(self.filter(sentence))
        else:
            f=FilterDB()
            f.addWord(sentence)

    def filter(self,sentence):
        s_words=sentence.split(' ')
        x=FilterDB()
        b_words=x.getAll()
        if b_words==False or b_words==True:
            return "My memory has not yet been sorted"
        else:
            for word in s_words:
                for w in b_words:
                    if w==word:
                        return False
        return True

##memory bank for the Filtration
class FilterDB:
    def __init__(self):
        try:
            self.db=sqlite3.connect('./Memory/blacklist.db')
        except:
            from Resources import Resources
            r=Resources('./Memory/blacklist.db')
    def getAll(self):
        conn=self.db.cursor()
        sql="SELECT * from blacklist;"
        try:
            words=conn.execute(sql)
            return words
        except:
            from resources import Resources
            r=Resources('./Memory/blacklist.db')
            return False

    def addWord(self,word):
        word=word.split(' ')
        conn=self.db.cursor()
        if len(word)>1:
            for w in word:
                sql="INSERT into blacklist (word) values('"+w+"');"
                try:
                    conn.execute(sql)
                    self.db.commit()
                except:
                    return False
            return True
        else:
            word=word[0]
            sql="INSERT into blacklist (word) values('"+word+"');"
            try:
                conn.execute(sql)
                self.db.commit()
                return True
            except:
                print("Error")
                return False