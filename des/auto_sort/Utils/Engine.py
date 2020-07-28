import json
class Notification:
    @staticmethod
    def success(message):
        Notification.output("Success: "+str(message))

    @staticmethod
    def error(message):
        Notification.output("Error: "+str(message))

    @staticmethod
    def notif(message):
        Notification.output(message)

    @staticmethod
    def loading():
        pass

    @staticmethod
    def output(message):
        print(str(message))

class Logs:
    @staticmethod
    def log_error(message):
        pass
    @staticmethod
    def log(message):
        pass
    @staticmethod
    def get_curr_time():
        pass

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
            Notification.error("Permission error while reading file"+str(filepath))
        except:
            Notification.error("Unexpected error while reading file"+str(filepath))
        return data

    @staticmethod
    def cut_file(source_path,destination_path):
        pass

    @staticmethod
    def copy_file(source_path,destination_path):
        pass

    @staticmethod
    def file_exists(file_name,destination_path):
        pass

    @staticmethod
    def delete_file(file_path):
        pass 

class Storage(Files):
    @staticmethod
    def get_free_space(dir_path):
        pass

    @staticmethod
    def get_file_size(file_path):
        pass

    @staticmethod
    def standardize_bytes(bytes):
        pass

    @staticmethod
    def file_fits(dir_path,file_path):
        pass