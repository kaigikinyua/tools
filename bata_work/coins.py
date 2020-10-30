import os
import shutil
class Files:
    @staticmethod
    def copy_file(filepath,copypath):
        try:
            shutil.copy(filepath,copypath)
            return True
        except:
            return False
    @staticmethod
    def rename_file(filepath,newname):
        try:
            os.rename(filepath,newname)
            return True
        except:
            return False
    @staticmethod
    def is_folder(folderpath):
        if(os.path.isdir(folderpath)):
            return True
        return False
    
    @staticmethod
    def is_file(filepath):
        if(os.path.isfile(filepath)):
            return True
        return False
    
    @staticmethod
    def file_exists(filepath):
        if(Files.is_file(filepath)):
            return True
        Messages.error("File {f} does not exist".format(f=filepath))
        return False

    @staticmethod
    def folder_exists(folderpath):
        if(Files.is_folder(folderpath)):
            return True
        Messages.error("Folder {f} does not exist".format(f=folderpath))
        return False

    @staticmethod
    def open_file_explorer(path):
        ProcessExec.run_command("explorer {p}".format(p=path))

#TODO<Renaming folder>
#TODO<delete file>
#TODO<create a logging class|mechanism>

class ProcessExec:
    @staticmethod
    def run_setup(path):
        try:
            result=ProcessExec.run_command("\\{ex}".format(ex=path))
            if(result==True):
                pass
            else:
                Messages.error("Setup {ex} encounterd an error while executing".format(ex=path))
        except:
            Messages.error("Could not run setup {ex}".format(ex=path))
    @staticmethod
    def run_command(command):
        try:
            x=os.system(command)
            if(x==0):
                return True
            else:
                Messages.error("The system encounterd an error while running the command {c}".format(c=command))
                return False
        except:
            Messages.error("Could not execute command {c}".format(c=command))
            return False

class Messages:
    @staticmethod
    def message(message):
        print(message)
    @staticmethod
    def warning(message):
        print("!!Warning!!-----{m}".format(m=message))
        #log warnings
    @staticmethod
    def error(message):
        print("!!Error:==={message}===".format(message=message))
        #log errors
    @staticmethod
    def success(message):
        print(message)
        #log success
    @staticmethod
    def prompt(message):
        message=str(message)
        ans=input("{m}".format(m=message))
        return ans

class Coins:
    def is_pre_install(self):
        ans=Messages.prompt("Have you already installed coins on this Computer\ny/n\n->")
        if(ans.lower()=="y"):
            return False
        return True

    def post_install(self):
        #prompt to run ./assets/paths.reg_file
        #check platform in order to run dev patch
        #copy the files to the recommended folders
        #create shorcut to start in [Coins start folder]
        #access coins folder
        pass

    def pre_install(self):
        #rename orant folder in C:\Orant to C:\Orant_Prev
        #navigate to bgeneral and run set_up
        #open manual on notepad
        pass

    @staticmethod
    def backup_orant_folder():
        if(Files.is_folder("C:\\orant") or Files.is_folder("C:\\Orant")):
            renamed=Files.rename_file("C:\\orant","C:\\orant_backup")
            if(renamed):
                return True
            return False
        return True
        

    def registry_variables(self):
        #run [reg import path to file -> ./assets/paths.reg]
        pass

    @staticmethod
    def copy_shorcut():
        pass

    def coins_platform_version(self):
        platform=Messages.prompt("Which windows platform version is this computer running on\n1.Windows 10 \n2.Windows 7\n->")
        if(int(platform)==2):
            Coins.developer_patch()
    
    @staticmethod
    def developer_patch():
        pass

if __name__=="__main__":
    Messages.message("<=============Coins installer===============>")
    coins=Coins()
    if(coins.is_pre_install()==False):
        coins.post_install()
    else:
        coins.pre_install()