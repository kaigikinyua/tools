from Utils.Engine import Files
class SetUp:
    @staticmethod
    def setup_resources():
        dir_list=['./Logs','./Logs/scaned_dir','./dir_dist.json','./key_words.json']
        file_list=['./Logs/errors.txt','./Logs/program.txt']
        for directory in dir_list:
            Files.create_dir(directory)
        for f in file_list:
            Files.create_file(f)

    @staticmethod
    def factory_reset():
        pass

    @staticmethod
    def setup_words():
        pass

class ScanResources(SetUp):
    pass