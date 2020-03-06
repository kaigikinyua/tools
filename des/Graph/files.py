import os
class Files:
    def create_database_folder(self,foldername):
        if (self.check_if_exists('./UsersDatabase/'+foldername)==True):
            return False
        else:
            try:
                os.mkdir('./UsersDatabase/'+foldername)
                #add database to logs
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
                #add filename to logs
            except:
                return False

    def write_data_to_file(self,databasename,filename,parameter,data):
        try:
            filepath='./UsersDatabase/databasename/filename'
            x=open(filepath,'w')
            x.write(data)
            x.close()
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
    
    def json_response(self,data):
        pass
    def parse_input_data(self,data):
        pass