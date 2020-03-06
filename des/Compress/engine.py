class Engine:
    ratio=[2,4,8,12,16]
    def __init__(self):
        filename=input("Which file would you like to compress?\n")
        f=open(filename,'r')
        f_data=f.readlines()
        f.close()
        self.compress(f_data)
    def compress(self,data):
        print("compressing...")
        i=0
        chunks=[]
        chunk=""
        for d in data[0]:
            if(i<2):
                chunk+=d
                i+=1
            else:
                chunks+=[chunk]
                chunk=""
                i=0
        print(len(data[0]))
        print(len(chunks))
        self.wordstack(chunks)
    def wordstack(self,chunks):
        print("Word stack")
        i=0;stack={}
        matches=0
        chunks_copy=chunks
        for chunk in chunks:
            while i<len(chunks):
                if i>0:
                    if chunk==chunks[i]:
                        if chunk in stack:
                            stack[chunk]+=[i+matches]
                        else:
                            stack[chunk]=[]
                            stack[chunk]+=[i+matches]
                        del chunks[i]
                        matches+=1
                i+=1
            i=0
        total=0
        f=open('keys','r')
        comp=f.readlines()
        f.close()
        print(chunks_copy)
        max=len(chunks_copy)
        for s in stack:    
            i=0;index=0
            if len(stack[s])>2:
                for rep in stack[s]:
                    if rep<max:
                        chunks_copy[rep]="a"
                        print("compressing")
        f=open("compressed",'a')
        for c in chunks_copy:
            f.write(c)
        f.close()
    def comp(self):
        pass
E=Engine()