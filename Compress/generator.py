import random
def generate():
    filename=input("Enter filename \n")
    f=open("keys",'r')
    keys=f.readlines()
    print(keys)
    f.close()
    data=""
    i=0
    for i in range(10000):
        x=len(keys[0])-1
        index=random.randrange(0,x)
        data+=keys[0][index]
    f=open(filename,'w')
    f.write(data)
    f.close()
generate()