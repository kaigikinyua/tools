from random import randrange
import json
import requests

class MyRandom:

    @staticmethod
    def random_users(number):
        R=MyRandom()
        names=R.get_mock_up_data("names")
        domains=R.get_mock_up_data("email_domains")
        Gen_Users=[]
        if(names!=False and domains!=False): 
            for i in range(number):
                s=randrange(0,2)
                f_name="";l_name=""
                if(s==0):
                    f_name=names[0]["male_first"][randrange(0,len(names[0]["male_first"]))]
                    l_name=names[1]["male_last"][randrange(0,len(names[1]["male_last"]))]
                else:
                    f_name=names[2]["female_first"][randrange(0,len(names[2]["female_first"]))]
                    l_name=names[3]["female_last"][randrange(0,len(names[3]["female_last"]))]
                r_domain=randrange(0,3)
                d=""
                if(r_domain<1):
                    d=domains[0]["gmail"]
                else:
                    d=domains[1]["yahoo"]
                email=f_name.lower()+l_name.lower()+d
                user=f_name+" "+l_name
                Gen_Users.append({"username":user,"email":email})
            return Gen_Users
        else:
            print("Error while getting usernames and domains from ./Data.json")
            print(names)
            print(domains)
            return False 
    
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
    def random_pass(number,pass_size):
        passwords=[]
        R=MyRandom()
        characters=R.get_mock_up_data('charcters')
        if(characters!=False):
            for i in range(number):
                alpha=characters[0]["alpha"][0:randrange(0,len(characters[0]["alpha"]))]
                numbers=characters[1]["numbers"][0:randrange(0,len(characters[1]["numbers"]))]
                special=characters[2]["special"][0:randrange(len(characters[2]["special"]))]
                password=alpha+str(numbers)+special
                passwords.append(password)
            return passwords
        else:
            print("Error getting characters for passwords")
            print(characters)
            return False
    def get_mock_up_data(self,field):
        try:
            with open('Data.json','r') as f:
                data=json.load(f)
                return data[field]
        except:
            return False

    def save_data(self,filename):
        pass

class Distribution:
    
    @staticmethod
    def web(url):
        pass 
    
    @staticmethod
    def tcp(ip,port):
        pass 
    
    @staticmethod
    def mysql_database(databasename,table_name):
        pass 

class Errors:
    
    @staticmethod
    def error_message(message):
        pass 


print(MyRandom.random_pass(10,10))