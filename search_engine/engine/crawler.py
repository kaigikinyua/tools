import requests
from utilities.Util import Files
class WebPage:
    def __init__(self,url):
        self.url=url

    def get_webpage():
        res=None
        try:
            res=requests.get(self.url)
        except:
            print("Error while fetchnig webpage {u}".format(u=self.url))
            res=None
        if(res.status_code==200):
            return res
        else:
            print("Status code {c} for site {s}".format(c=res.status_code,s=self.url))
            return res,status_code


class Crawler:
    def __init__(self):
        self.parsed_urls=[];self.unparsed=[]
    def parse_url(self):
        f=Files("../data/urls.json")
        data=f.loadJson()
        self.unparsed=data["uncrawled"]
        print(self.unparsed)
        #get webpage
    
    #strip data [title,image,icon,intro]
    #keywords
    #save parsed url data to db/file
    #append to parsed_url

if __name__=="__main__":
    c=Crawler()
    c.parse_url()



    
    
            