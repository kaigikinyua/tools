import os
import shutil
class Files:
    @staticmethod
    def copy_file(self,filepath,copypath):
        try:
            shutil.copy(filepath,copypath)
            return True
        except:
            return False
    #delete file
    @staticmethod
    def rename_file(self,filepath,newname):
        try:
            os.rename(filepath,newname)
            return True
        except:
            return False
    
    @staticmethod 
    def rename_folder(self,folderpath):
        pass
    
    @staticmethod
    def is_folder(self,folderpath):
        if(os.path.isdir(folderpath)):
            return True
        return False
    
    @staticmethod
    def is_file(self,filepath):
        if(os.path.isfile(filepath)):
            return True
        return False
    
    @staticmethod
    def file_exists(self,filepath):
        if(Files.is_file(filepath)):
            return True
        Messages.error("File {f} does not exist".format(f=filepath))
        return False

    @staticmethod
    def folder_exists(self,folderpath):
        if(Files.is_folder(folderpath)):
            return True
        Messages.error("Folder {f} does not exist".format(f=folderpath))
        return False
#TODO create a logging system
class ProcessExec(Files):
    def run_setup():
        pass

class Messages:
    @staticmethod
    def message(message):
        print(message)
    @staticmethod
    def error(message):
        print("Error:==={message}===".format(message=message))
    @staticmethod
    def success(message):
        print(message)

class Coins:
    def install_phase(self):
        pass

    def post_install(self):
        pass

    def pre_install(self):
        pass

    def backup_orant_folder(self):
        pass

    def registry_variables(self):
        pass

    def create_shorcut(self):
        pass

    def coins_platform_version(self):
        pass

    def developer_patch(self):
        pass

if __name__=="__main__":
