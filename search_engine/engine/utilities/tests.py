#import unit test
import unittest
import os
import json
from Util import Files
class FilesTest(unittest.TestCase):

    def setUp(self):
        self.data=None
        try:
            os.path.isfile("tests.json")
            with open("tests.json","r") as f:
                self.data=json.load(f)
        except:
            print("Error while locating test.json")
        #f=open("dump.json",'w')
        #f.close()

    def test_loadJson(self):
        f=Files("tests.json")
        data=f.loadJson()
        self.assertEqual(data,self.data)

    def test_exportJson(self):
        f=Files("dump.json")
        d=f.exportJson(self.data)
        #self.assertEqual(d,True)
        dump_data=f.loadJson()
        t=Files("tests.json")
        prev_data=t.loadJson()
        self.assertEqual(prev_data,dump_data)

if __name__=="__main__":
    unittest.main()