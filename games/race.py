from random import randrange
import time
import threading
class Race:
    def __init__(self):
        #get racers from db
        self.drivers=['James','Antony','John','Gabriel']
        self.sequence=[]
        self.times=[]
        ans=input("Drivers are you ready\n")
        if ans=='y':
            #ready set and go
            print("Start")
            for d in self.drivers:
                t=threading.Thread(target=self.lap,name="racing",args=(d,))
                t.start()

    def driverTimes(self):
        print("Lap time for --- is ----")

    def lap(self,drivername):
        seconds=randrange(1,10)
        time.sleep(seconds)
        self.times+=[seconds]
        self.sequence+=[drivername]
        if len(self.sequence)==len(self.drivers):
            self.results()
    def results(self):
        for i in range(len(self.sequence)):
            if self.sequence[0]==self.sequence[i]:
                print("\n\n\n\t"+self.sequence[i]+" has won the race !!!!\n\n\n<===========>")
                print(self.sequence[i]+" position:"+str(i+1)+" time:"+str(self.times[i]))
            else:
                print(self.sequence[i]+" position:"+str(i+1)+" time:"+str(self.times[i]))
R=Race()