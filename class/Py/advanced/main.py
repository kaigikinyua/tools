import sys
import time

def launch_rocket():
    print("Getting ready to lauch rocket")
    time.sleep(1)
    run_diagnostics()
    check_weather()
    print("We have lift off")

def run_diagnostics():
    print("Starting diagnostics ....")
    time.sleep(2)
    checkList=['Booster Rocket 1','Booster rocket 2','Fuel capacity','Communications','Conrolls','Co-odinates']
    for check in checkList:
        print("checking "+check) 
        time.sleep(1)
        print("clear-------")
    print("We are good")

def check_weather():
    checkList=['Cloud coverage','Wind speeds','Debree']
    for check in checkList:
        print("Analyzing "+check)
        time.sleep(2)
        print(check+" is good")

tasks=sys.argv
if(tasks[1]=='launch'):
    launch_rocket()
elif(tasks[1]=='diagnosis'):
    run_diagnostics()
elif(tasks[1]=='weather'):
    check_weather()
else:
    print(sys.argv)
    print("You passed no arguments")