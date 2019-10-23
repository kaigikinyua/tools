import sqlite3
class DB:

    def getDrivers(self):
        c=self.connectToDb('./AppData/drivers.db')
        d=c.cursor()
        d.execute("SELECT * FROM Drivers")
        drivers=d.fetchall()
        for driver in drivers:
            print(driver)
    def getCarSettings(self,id):
        c=self.connectToDb('./AppData/car')
    def getTrackDetails(self):
        print(" track details are")

    def connectToDb(self,dbPath):
        try:
            conn=sqlite3.connect(dbPath)
            return conn
        except:
            return False
D=DB()
D.getDrivers()