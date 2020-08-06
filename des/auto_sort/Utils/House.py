from Utils.Engine import Files
import os
import shutil
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
        if(os.path.isdir("./Reset_Logs")!=True):
            os.mkdir("./Reset_Logs")
        resets=os.listdir("./Reset_Logs")
        num=0
        for reset in resets:
            r=reset.split('_')
            num=r[len(r)-1]
            num=int(num+1)
        new_reset="./Reset_Logs/version_"+str(num)
        os.mkdir(new_reset)
        back_up=['./dir_dist.json','./key_words.json','./Logs']
        for b in back_up:
            if(os.path.isfile(b)):
                shutil.copy(b,new_reset)
            elif(os.path.isdir(b)):
                print("Implement copy file contents")

                

class ScanResources(SetUp):
    pass