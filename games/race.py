from random import randrange
import time
import threading

#code imports
from db import *

class Race:
    def __init__(self):
        #get racers from db
        d=DB()
        self.drivers=d.selectAllDrivers()
        self.sequence=[]
        self.times=[len(self.drivers)-1][6]
        ans=input("Drivers are you ready\n")
        if ans=='y':
            #ready set and go
            print("Start")
            laps=0
            while laps<4:
                for d in self.drivers:
                    t=threading.Thread(target=self.lap,name="racing",args=(d[0],laps))
                    t.start()
                laps+=1

    def driverTimes(self):
        print("Lap time for --- is ----")

    def lap(self,drivername,lapNum):
        seconds=randrange(1,10)
        time.sleep(seconds)
        self.times[drivername][lapNum]=seconds
        self.sequence+=[drivername]
        if len(self.sequence)==len(self.drivers):
            self.results(lapNum)

    def results(self,lapNum):
        #take the totals of all the laptimes the least is the winner
        for driver in self.drivers:
            i=0;totalLapTime=0
            while i<=lapNum:
                totalLapTime+=self.drivers[driver][lapNum]
            self.drivers[driver][lapNum+1]=totalLapTime
        
        max=len(self.times[self.drivers[0][0]]-1)
        for driver in self.drivers:

            for i in range(len(self.drivers)-1):
                if i<max:        
                    print(driver+" "+self.times[driver][max])
        
        if self.sequence[0]==self.sequence[i]:
            print("\n\n\n\t"+self.sequence[i]+" has won the lap "+str(lapNum)+"!!!!\n\n\n\t<===========>")
            print(self.sequence[i]+" position:"+str(i+1)+" time:"+str(self.times[i]))
        else:
            print(self.sequence[i]+" position:"+str(i+1)+" time:"+str(self.times[i]))

R=Race()