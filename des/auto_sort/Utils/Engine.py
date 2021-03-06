import json
import os
import shutil
import threading
class NotificationCodes:
    codes={"warning":"\033[94m","error":"\033[93m","success":"\033[92m","normal":"\033[0m"}
class Notification:
    
    """def threaded(func):
        def innner_func(*args, **kwargs):
            t=threading.Thread(target=func,args=(*args, **kwargs))
            t.start()
        return innner_func
    """
    def outputCover(inner_func):
        def inner_func(*args, **kwargs):
            print(NotificationCodes.codes[normal])
        return inner_func

    @staticmethod
    @outputCover
    def success(message):
        Notification.output(NotificationCodes.codes["success"]+"Success: "+str(message))
    
    @staticmethod
    @outputCover
    def error(message):
        Notification.output(NotificationCodes.codes["error"]+"Error: "+str(message))

    @staticmethod
    def notif(message):
        Notification.output(NotificationCodes.codes["warning"]+str(message))

    #@threaded
    @staticmethod
    def loading(message):
        anim=[".","..","...","..."]
        i=0
        while True:
            if(i<len(anim)):
                print(str(message)+anim[i],end="\r")
            else:
                i=0

    @staticmethod
    def output(message):
        print(str(message))

    @staticmethod
    def warning(message):
        print(str(message))
class Logs:
    @staticmethod
    def log_error(message):
        error={"time":Logs.get_curr_time(),"message":message}
        Files.append_to_file("./Logs/errors.txt",error)
    @staticmethod
    def log(message):
        log={"time":Logs.get_curr_time(),"message":message}
        Files.append_to_file("./Logs/program.txt")
    @staticmethod
    def get_curr_time():
        from datetime import datetime
        return datetime.now()

class Files:
    @staticmethod
    def load_json(file_path):
        data=False
        try:
            with open(file_path,"r") as f:
                data=json.load(f)
        except:
            #deal with json exeptions
            Files.read_file(file_path)
        return data

    @staticmethod
    def write_json(file_path,data):
        file_exists=Files.read_file(file_path)
        if(file_exists==False):
            pass
            #Files.create_file(file_path)
        else:
            data=file_exists+data
        try:
            json.dumps(data,file_path)
        except:
            #deal with json exeptions
            Files.read_file(file_path)
        #return state


    @staticmethod
    def append_to_file(filepath,data):
        done=False
        try:
            f=open(filepath,"a")
            f.write(data)
            f.close()
            done=True
        except FileNotFoundError:
            Notification.error("Could Not find file"+str(filepath))
        except PermissionError:
            Notification.error("Permission error")
        except:
            Notification.error("Unexpected error while trying to write to file"+str(filepath))
        return done

    @staticmethod
    def read_file(filepath):
        data=False
        try:
            f=open(filepath,"r")
            data=f.readlines()
            f.close()
        except FileNotFoundError:
            Notification.error("Could Not find the file"+str(filepath))
        except PermissionError:
            Notification.error("Permission error while reading file\n"+str(filepath))
        except:
            Notification.error("Unexpected error while reading file\n"+str(filepath))
        return data

    @staticmethod
    def create_file(filepath):
        file_created=False
        file_exists=Files.read_file(filepath)
        if(file_exists==False):
            try:
                f=open(filepath,"w")
                f.close()
                file_created=True
            except PermissionError:
                Notification.error("Not enough permissions to create the file\n"+str(filepath))
            except:
                Notification.error("An error ocurred while creating the file\n"+str(filepath))
        return file_created        


    @staticmethod
    def cut_file(source_path,destination_path):
        if(Files.copy_file(source_path,destination_path)==True):
            Files.delete_file(source_path)
            return True
        else:
            return False

    @staticmethod
    def copy_file(source_path,destination_path):
        res=False
        try:
            shutil.copy(source_path,destination_path)
            res=True
        except FileExistsError:
            Notification.error("File "+str(source_path)+"already exists in the directory "+str(destination_path))
        except:
            Notification.error("Failed to copy file "+str(source_path)+" to "+str(destination_path))
        return res
    @staticmethod
    def file_exists(file_path):
        if(os.path.isfile(file_path)):
            return True
        else:
            return False

    @staticmethod
    def delete_file(file_path):
        if(Files.file_exists(file_path)):
            ans=Notification.warning("\a Do you want to delete file?\ny/n")
            if(ans=="y" or ans=="Y"):
                os.remove(file_path)
        else:
            Notification.error(str(file_path)+" does not exists")
    
    @staticmethod
    def batch_delete(file_paths):
        for f in file_paths:
            if(os.path.isfile(f)):
                try:
                    os.remove(file_paths)
                except FileNotFoundError:
                    Notification.error(str(f)+" does not exist")
                except PermissionError:
                    Notification.error("Permission error while deleting the file"+str(f))
                except:
                    Notification.error("A problem occurred while trying to delete the file"+str(f))
            elif(os.path.isdir(f)):
                pass
            else:
                Notification.error("Unknown directory content "+str(f))
    
    @staticmethod
    def create_dir(path):
        created_dir=False
        if(os.path.isdir(path)==False):
            try:
                os.mkdir(path)
                created_dir=True
            except PermissionError:
                Notification.error("Not enough permissions to create directory\n"+str(path))
            except:
                Notification.error("An error ocurred while trying to create the directory "+str(path))
        return created_dir
    @staticmethod
    def list_dir_contents(dir_path):
        if(os.path.isdir(dir_path)):
            contents=os.listdir(dir_path)
            return contents
        else:
            return []

class Storage(Files):
    @staticmethod
    def get_free_space(dir_path):
        total,used,free=shutil.disk_usage(dir_path)
        free_disk_space=Storage.standardize_bytes(free)
        return free_disk_space

    @staticmethod
    def get_file_size(file_path):
        return os.path.getsize(file_path)

    @staticmethod
    def standardize_bytes(bytes_size):
        kb=1024
        mb=kb*1024
        gb=mb*1024
        file_size=0;metric=""
        if(bytes_size<kb):
            file_size=float(bytes_size/kb)
            metric="KB"
        elif(bytes_size>mb and bytes_size<gb):
            file_size=float(bytes_size/mb)
            metric="MB"
        else:
            file_size=float(bytes_size/gb)
            metric="GB"
        return {"size":file_size,"metric":metric,"bytes":bytes_size}

    @staticmethod
    def file_fits(dir_path,file_path):
        free_space=Storage.get_free_space(dir_path)
        file_size=Storage.get_file_size(file_path)
        if(free_space["bytes"]>file_size["bytes"]):
            return True
        else:
            return False