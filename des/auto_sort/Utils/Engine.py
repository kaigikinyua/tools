import json
class Notification:
    @staticmethod
    def success(message):
        pass
    @staticmethod
    def error(message):
        pass
    @staticmethod
    def notif(message):
        pass
    @staticmethod
    def loading():
        pass

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
        pass
    @staticmethod
    def write_json(file_path,data):
        pass

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