options=['use']
crud=['create','select','update','delete']
context=['database','entity','node','relationship']
class Parser:
    """
        commands
            options=[use]
            crud=[create,select,update,delete]
            context=[database,entity,node,relationship]
            g=<crud><context>
            o=<use>database<dbname>
    """
    
    def commands(self,command):
        first=options+crud
        cmds=command.split(" ")
        if len(cmds)==0:
            return "Enter A command"
        else:
            for i in range(len(first)):
                if(i==len(crud)):
                    return "Command "+cmds[0]
                else:
                    if(cmds[0].lower()==first[i-1]):
                        pass