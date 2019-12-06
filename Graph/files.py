import os
class Files:
    def create_database_folder(self,foldername):
        if (self.check_if_exists('./UsersDatabase/'+foldername)==True):
            return False
        else:
            try:
                os.mkdir('./UsersDatabase/'+foldername)
                return True
            except:
                return "Error writing in the directory"

    def create_file(self,databasename,filename):
        if(self.check_if_exists('./UsersDatabase/'+databasename+'/'+filename+".json")):
            return False
        else:
            try:
                f=open('./UsersDatabase/'+databasename+"/"+filename+".json",'w')
                f.close()
            except:
                return False

    def read_whole_file(self,databasename,file):
        try:
            x=open('./UsersDatabase/'+databasename+"/"+filename+".json",'r')
            data=x.readlines()
            x.close()
            return data
        except:
            return False

    def check_if_exists(self,path):
        if os.path.isdir(path):
            return True
        elif(os.path.isfile(path)):
            return True
        else:
            return False

f=Files()
f.create_database_folder('FirstDatabase')
f.create_file('FirstDatabase','first_file')