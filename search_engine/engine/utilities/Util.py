import json
import os
class Files:
    def __init__(self,filepath):
        self.filepath=filepath

    def loadJson(self):
        data=None
        try:
            with open(self.filepath,"r") as f:
                data=json.load(f)
        except:
            print("Error while loading json from file {f}".format(f=self.filepath))
        return data

    def exportJson(self,data):
        try:
            with open(filepath,"w") as f:
                json.dump(f,data)
        except:
            print("Error while exporting data to file {f}".format(f=self.filepath))

class Messages:
    @staticmethod
    def error(message):
        print("Error: {m}".format(m=message))
    @staticmethod
    def warning(message):
        print("Warning: {m}".format(m=message))
    
    @staticmethod
    def success(message):
        print("Sucess: {m}".format(m=message))
"""
class Logger:
    def log(self,logfile):
        def decorator(*args,**kwargs):
            def inner_func(func):
                func(*args,**kwargs)
                return func
            return inner_func
        return decorator
"""