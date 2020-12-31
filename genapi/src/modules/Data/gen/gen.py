from random import randrange
import json
import requests

class MyRandom:
    @staticmethod
    def random_users(number):
        male_names=MyRandom.get_mock_up_data("male")
        female_names=MyRandom.get_mock_up_data("female")
        Gen_Users=[]
        if(male_names!=False and female_names!=False): 
            for i in range(number):
                rand_gender=randrange(0,3)
                f_name="";l_name=""
                if(rand_gender==0):
                    user=MyRandom.gen_user(male_names)
                else:
                    user=MyRandom.gen_user(female_names)

                domains=MyRandom.get_mock_up_data("emails")
                d=domains[randrange(0,len(domains))]["domain"]
                
                user["email"]=user["firstname"].lower()+user["lastname"].lower()+d
                Gen_Users.append(user)
        else:
            print("Error while getting usernames and domains from ./users.json")
            Gen_Users=False
        return Gen_Users
    
    @staticmethod
    def gen_user(dataset):
        fNameSize=len(dataset[0]["first"])#-1
        lNameSize=len(dataset[1]["last"])#-1
        f_name=dataset[0]["first"][randrange(0,fNameSize)]["name"]
        l_name=dataset[1]["last"][randrange(0,lNameSize)]["name"]
        password=MyRandom.random_pass(8)
        return {"username":"{f} {l}".format(f=f_name,l=l_name),"firstname":f_name,"lastname":l_name,"email":"","password":password}

    @staticmethod
    def random_phone(number,digits):
        phone_numbers=[]
        for i in range(number):
            phone=randrange(0,digits)
            phone_numbers.append(phone)
        return phone_numbers
    @staticmethod
    def random_age(number,age_range):
        ages=[]
        for i in range(number):
            age=randrange(0,age_range+1)
            ages.append(age)
        return ages 
    
    @staticmethod
    def random_pass(pass_size):
        password=None
        characters=MyRandom.get_mock_up_data('charcters')
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
    def get_mock_up_data(field):
        try:
            with open('names.json','r') as f:
                data=json.load(f)
                return data[field]
        except:
            return False

    @staticmethod
    def save_data(filename):
        pass

if __name__=="__main__":
    print("Generating users....")
    users=MyRandom.random_users(100)
    for user in users:
        print(user) 
