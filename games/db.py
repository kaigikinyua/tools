import sqlite3
class DB:

    def getDriver(self,id):
        c=self.connectToDb('./AppData/drivers.db')
        d=c.cursor()
        d.execute("SELECT * FROM Drivers where number="+id+";")
        drivers=d.fetchall()
        print(drivers)

    def getCarSettings(self,id):
        c=self.connectToDb('./AppData/drivers.db')
        d=c.cursor()
        d.execute("SELECT * FROM cars where DriverNumber="+id+";")
        carsettings=d.fetchall()
        for car in carsettings:
            print(car)

    def getTrackDetails(self,id):
        c=self.connectToDb('./AppData/tracks.db')
        d=c.cursor()
        d.execute("SELECT * FROM trac where tracknumber="+id+";")
        trac=d.fetchall()
        print(trac)


#SELECT ALL
    def selectAllTracs(self):
        print("tracs")
    def selectAllDrivers(self):
        d=self.connectToDb('./AppData/drivers.db')
        c=d.execute("SELECT * FROM Drivers;")
        drivers=c.fetchall()
        for driver in drivers:
            print(driver)
        return drivers

    def selectAllCars(self):
        print("Cars")
    def selectAllTeams(self):
        print("Teams")


#universal query
    def universal(self,db,query,params):
        c=self.connectToDb(db)
        d=c.cursor()
        d.execute(query)
        data=d.fetchall()
        return data

#connection to the database
    def connectToDb(self,dbPath):
        try:
            conn=sqlite3.connect(dbPath)
            return conn
        except:
            return False