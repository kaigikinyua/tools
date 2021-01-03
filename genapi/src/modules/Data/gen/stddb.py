import json

class Database:
    @staticmethod
    def gen_schema(data):
        pass
    @staticmethod
    def std_schema(filename):
        pass


if __name__=="__main__":
    test_json={
        "users":[
            {"name":"antony","age":100,"sites":[{"name":"youtube"}]}
            ],
        "languages":[
            {"country":"Kenya","lang":[{"name":"Swahili"},{"name":"English"}]}
        ]
    }
    for elm in test_json:
        print(test_json[elm][0].keys())
