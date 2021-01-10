import json
import os
class Files:
    def __init__(self,filepath):
        self.filepath=filepath
        print(os.getcwd())
    def loadJson(self):
        data=None
        #try:
        with open(self.filepath,"r") as f:
            data=json.load(f)
        #except:
        #    print("Error while loading json from file {f}".format(f=self.filepath))
        return data

    def exportJson(self,data):
        try:
            with open(filepath,"w") as f:
                json.dump(f,data)
        except:
            print("Error while exporting data to file {f}".format(f=self.filepath))
