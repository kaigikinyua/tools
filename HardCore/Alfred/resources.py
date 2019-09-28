import os
import json
class Resources:
    def __init__(self,filepath):
        if os.path.isfile(filepath):
            print("Resource is present")
        else:
            print("resource absent")
            self.map(filepath)
    def map(self,filepath):
        self.extension(filepath)

    def extension(self,filepath):
        e=filepath.split('.')
        ext=e[len(e)-1]
        use=""
        if(ext=="db"):
            use="./Blueprint/Databases.json"
            type="database"
            print("trying to create database")
            return True
        else:
            print("Area Still under Construction")
    def createResource(self,resource,type):
        with open(resource,'r') as file:
            c=json.load(file)
            print(c)
            file.close()
            if(type=="database"):
                print("Creating databse")
            else:
                print("Construction")

class AdminSql:
    import sqlite3
    def __init__(self,dbpath,commad):
        try:
            self.db=sqlite3.connect(dbpath)
            c=self.db.cursor()
            try:
                c.execute(commad)
                self.db.commit()
            except:
                print("Error while admin was trying to run command "+commad)
        except:
            print("Error while admin creating database"+dbpath)

