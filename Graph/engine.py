
class Entities:
    def create_database(self,databasename):
        pass
    def create_Entity(self,nodename):
        pass
    def delete_Entity(self,nodename):
        pass
    def read_Entities(self,nodename):
        pass

class Crud(Entities):
    def get_Node(self,nodename,parameters):
        pass
    def update_Node(self,nodename,parameters):
        pass
    def delete_Node(self,nodename,parameters):
        pass
    def create_Node(self,nodename,parameters):
        pass

class Filters:
    def get_node(self,dataset,parameter):
        pass
    def get_relative(self,dataset,parameter):
        pass