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
