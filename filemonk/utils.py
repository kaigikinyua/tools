import os
class Directory:
    def __init__(self,directory):
        self.directory=directory

    def listFiles(self):
        contents=os.listdir(self.directory)
        files=[]
        for c in contents:
            if(os.path.isfile("{dir}/{c}".format(dir=self.directory,c=c))):
                files+=[c]
        return files

    def listDirectories(self):
        contents=os.listdir(self.directory)
        folders=[]
        for c in contents:
            if(os.path.isfolder("{dir}/{c}".format(dir=self.directory,c=c))):
                files+=[c]
        return folders


class Messages:
    @staticmethod
    def error(message):
        pass

    @staticmethod
    def success(message):
        pass

    @staticmethod
    def warning(message):
        pass

    @staticmethod
    def consoleLog(message,color=None):
        print("{m}\n".format(m=message))