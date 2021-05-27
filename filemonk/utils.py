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

class Files(Directory):
    def __init__(self,filepath):
        #super(directory)
        self.filepath=filepath
    
    def copyFile(self,destinationDir):
        if(os.path.isdir(destinationDir)):
            commands=PlatForm()
            #copy file to the destination
        else:
            Messages.error("Error: Destination {d} is not a valid directory".format(d=destinationDir))
        return False
    
    def deleteFile(self):
        pass

    def createDir(self):
        pass

    def deleteDir(self):
        pass

class PlatForm:
    windows={
        "copyFile":"copy {src} {dest}",
        "deleteFile":"",
        "createFolder":"mkdir {folder}",
        "deleteFolder":""
    }
    linux={
        "copyFile":"cp {src} {dest}",
        "deleteFile":"rm {file}",
        "createFolder":"mkdir {folder}",
        "deleteFolder":"rm -r {folder}"
    }
    def __init__(self):
        #run platform checks and return the correct commands
        pass

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