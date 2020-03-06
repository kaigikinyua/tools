import os
class Logs:
    def log(self,logtype,destination,data):
        if(logtype=='simple'):
            if(os.path.isfile):
                x=open(destination,'a')
                x.write(data)
                x.close() 
            else:
                x=open(destination,'w')
                x.write(data)
                x.close()  