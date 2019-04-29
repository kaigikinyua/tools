class Messages():
    def message(self,state,message):
        #sucess
        if state.lower()!="s":
            return ":( error while: "+message
        else:
            return message+"....Done :)"
