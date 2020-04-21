class Compression:
    def compress(self,data):
        data_length=len(data)
        compressed=""
        repeated=""
        for i in range(data_length-1):
            if(i+1<data_length):
                count=1;j=i
                while(j+1<data_length and data[j]==data[j+1]):
                    count+=1
                    j+=1
                if(count>1 and repeated!=data[i]):
                    compressed+=data[i]+str(count)
                    repeated=data[i]
                elif(repeated==data[i]):
                    pass
                else:
                    compressed+=data[i]
                    repeated=data[j]
        print(data+" : "+str(len(data)))
        print(compressed+" : "+str(len(compressed)))
    def decompress(self):
        #cases
        #1.Read Char and separate numbers
        #2.If a num is followed by a num
        pass
c=Compression()
c.compress('ajflkjaegvnafaevarrweravauighsnnjjahafgsyughareuighnjkhsfiaujan')