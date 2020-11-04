import os
import shutil
from threading import *

"""
#final touches to help run on debug and prod mode
class SystemCommands:
    open_manual_command="iexplorer"
    open_file_explorer="start"
    execute="./"
"""

class Errors:
    error_logs=[]

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
                error="Setup {ex} encounterd an error while executing".format(ex=path)
                Errors.error_logs+={"error":error}
                Messages.error(error)
        except:
            error="Could not run setup {ex}".format(ex=path)
            Error.error_logs+={"error":error}
            Messages.error(error)
    @staticmethod
    def run_command(command):
        try:
            x=os.system(command)
            if(x==0):
                return True
            else:
                error="The system encounterd an error while running the command {c}".format(c=command)
                Errors.error_logs+={"error":error}
                Messages.error(error)
                return False
        except:
            error="Could not execute command {c}".format(c=command)
            Errors.error_logs={"error":error}
            Messages.error()
            return False

    @staticmethod
    def openExplorer(path):
        openExplorer=ProcessExec.run_command("start {p}".format(p=path))
        if(openExplorer):
            return True
        else:
            Messages.error("Could not open file explorer to {p}".format(path))
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
        #prompt to run ./assets/paths.reg_file #ProcessExec.run_command("./paths.reg")
        #check platform in order to run dev patch
        #prompt to add to which users desktop 
        #Messages.prompt("Select which user to add the shortcut to the desktop")
        #list users in a dictionary
        #ProcessExec.run_command("cp location of the shortcut to users desktop")
        #copy the files to the recommended folders
        #create shorcut to start in [Coins start folder]
        #access coins folder
        #post_install complete
        pass
    def pre_install(self):
        #rename orant folder in C:\Orant to C:\Orant_Prev
        Files.rename_file("./test/orant",'./test/orant_prev')
        win7=Coins.is_windows_7()
        runPatch=False
        if(win7):
            Messages.message("Running coins for windows 7")
            #ProcessExec.run_command("nautilus --browser /home/antony/Desktop")
            ProcessExec.run_command("./test/coinswin7/setup.sh")
        else:
            Messages.message("Running coins for windows 10")
            #ProcessExec.run_command("nautilus --browser /home/antony/Documents")
            ProcessExec.run_command("./test/coinswin10/setup.sh")
        #pre_install complete

    @staticmethod
    def backup_orant_folder():
        if(Files.is_folder("C:\\orant") or Files.is_folder("C:\\Orant")):
            renamed=Files.rename_file("C:\\orant","C:\\orant_backup")
            if(renamed):
                return True
            return False
        return True

    @staticmethod
    def copy_shorcut():
        print("Copying coins shortcut shorcut")

    @staticmethod
    def is_windows_7():
        platform=Messages.prompt("Which windows platform version is this computer running on\n1.Windows 10 \n2.Windows 7\n->")
        if(int(platform)==2):
            return True
        return False
    
    @staticmethod
    def developer_patch_location():
        Messages.warning("Running developer patch")
        #if(ProcessExec.openExplorer("Open to explorer to bgen\..\windows7 patch")):
        #    pass
        #else:
        #    Messages.error("Could not open location of dev patch")

if __name__=="__main__":
    Messages.message("<=============Coins installer===============>")
    coins=Coins()
    open_manual=Messages.prompt("Would you like to open the manual on a browser\ny/n\n->")
    if(open_manual.lower()=="y"):
        #TODO -> Browser should be its own process/thread
        browser=Thread(target=ProcessExec.run_command("firefox ./assets/coins.html"),args=())
        browser.start() 
        #Process.Exec.run_command("iexplorer ./assets/coins.html")   
    if(coins.is_pre_install()==False):
        coins.post_install()
    else:
        coins.pre_install()
    print(Errors.error_logs)