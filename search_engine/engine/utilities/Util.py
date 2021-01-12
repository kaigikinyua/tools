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
        #IOWrapper exception for unserialized json data
        except:
            Messages.error("Could not load json from {p}".format(p=self.filepath))
        return data

    def exportJson(self,data):
        res=False
        try:
            with open(self.filepath,"w") as f:
                json.dump(data,f)
                res=True
        except:
            Messages.error("Could not export json to {p}".format(p=self.filepath))
        return res

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