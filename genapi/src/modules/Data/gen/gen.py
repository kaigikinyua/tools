from random import randrange
import json
import requests

class Files:
    #feature:add mock up for profile photos
    @staticmethod
    def fetch_mock_up(field):
        try:
            with open('names.json','r') as f:
                data=json.load(f)
                return data[field]
        except:
            return False
    @staticmethod
    def export_users(filename,gen_data):
        exported=False
        try:
            with open(filename,'w') as f:
                d=json.dump({"users":gen_data},f)
            exported=True
        except:
            print("Error while exporting users to {f}".format(f=filename))
        return exported           

class User:
    @staticmethod
    def gen_fulluser(dataset):
        fNameSize=len(dataset[0]["first"])#-1
        lNameSize=len(dataset[1]["last"])#-1
        f_name=dataset[0]["first"][randrange(0,fNameSize)]["name"]
        l_name=dataset[1]["last"][randrange(0,lNameSize)]["name"]
        user={
            "username":"{f} {l}".format(f=f_name,l=l_name),
            "firstname":f_name,"lastname":l_name,
            "email":User.gen_email(f_name,l_name),
            "password":User.gen_pass(8),
            "phone":User.gen_phone(10)
        }
        return user
    @staticmethod
    def gen_pass(size):
        password=None
        characters=Files.fetch_mock_up('charcters')
        if(characters!=False):
            alpha=characters[0]["alpha"][0:randrange(0,len(characters[0]["alpha"]))]
            numbers=characters[1]["numbers"][0:randrange(0,len(characters[1]["numbers"]))]
            special=characters[2]["special"][0:randrange(len(characters[2]["special"]))]
            password=alpha+str(numbers)+special
        else:
            print("Error getting characters for passwords")
            print(characters)
            password=False
        return password

    @staticmethod
    def gen_email(f_name,l_name):
        domains=Files.fetch_mock_up("emails")
        email=None
        if(domains!=False):
            d=domains[randrange(0,len(domains))]["domain"]
            email=f_name.lower()+l_name.lower()+d
            return email
        else:
            email=False
        return email

    @staticmethod
    def gen_phone(size):
        phone=""
        for i in range(size):
            phone+=(str(randrange(0,10)))
        phone="+"+str(phone)
        return phone

    @staticmethod
    def gen_age():
        return randrange(0,100)

class MyRandom:
    @staticmethod
    def terminal_commands(*args, **kwargs):
        #number of users
        #usertypes
        
    @staticmethod
    def random_users(number):
        male_names=Files.fetch_mock_up("male")
        female_names=Files.fetch_mock_up("female")
        Gen_Users=[]
        if(male_names!=False and female_names!=False): 
            for i in range(number):
                rand_gender=randrange(0,3)
                if(rand_gender==0):
                    user=User.gen_fulluser(male_names)
                else:
                    user=User.gen_fulluser(female_names)
                Gen_Users.append(user)
        else:
            print("Error while getting usernames and domains from ./users.json")
            Gen_Users=False
        return Gen_Users

if __name__=="__main__":
    print("Generating users....")
    users=MyRandom.random_users(100)
    for user in users:
        print(user)
    ans=input("Export generated users?\ny/n")
    if(ans.lower()=="y"):
        ans=input("Enter file name to export to\n")
        if(len(ans)>0):
            export_state=Files.export_users(ans+".json",users)
            if(export_state==True):
                print("Export is successfull") 
