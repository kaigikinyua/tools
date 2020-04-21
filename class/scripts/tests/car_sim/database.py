import sqlite3

class DB:
    def __init__(self):
        try:
            self.db=sqlite3.connect('./DB/drivers.db')
        except:
            print("Error Connecting to database")
    
    def get_Driver_settings(self,id):
        sql="SELECT * FROM drivers where id ="+str(id);
        cursor=self.db.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()
        return  data
    def get_all_Drivers(self):
        sql="SELECT * FROM drivers;"
        cursor=self.db.cursor()
        cursor.execute(sql)
        data=cursor.fetchall()
        return data