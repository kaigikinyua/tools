from django.test import TestCase,Client

def response_check(func):
    def inner_function(*args, **kwargs):
        response=func(*args, **kwargs)
        if(response.status_code==200):
            print("{f} status code is 200".format(f=func.__name__))
    return inner_function
# Create your tests here.
class ViewsTest(TestCase):
    def setUp(self):
        self.c=Client()
    @response_check
    def test_index(self):
        response=self.c.get("/")
        return response
    @response_check
    def test_login(self):
        response=self.c.get("/login")
        return response



