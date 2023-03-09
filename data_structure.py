from collections import namedtuple, deque, defaultdict, ChainMap, Counter,UserDict,UserList, UserString

Book = namedtuple ('Book',['Name','Author'])

book1 = Book('The love of Basketball',"Kevin")


my_queue = deque([1,2,'Name'])

dd = defaultdict(int)

dict1 = {"data":1,"name":"Damn","gender":"female"}
dict2 = {"gender":"male","age":22}

chain = ChainMap(dict1,dict2)

inventory = Counter(['apple','banana','apple','banana','banana','banana','cat'])

class MyDict(UserDict):
    def push(self, key, value):
        raise RuntimeError("Cannot insert")
    
    def hiho(self):
        print('Hiiiii~Ho~')

d = MyDict({'ab':1,'bc':2,'cd':3})

class MyString(UserString):
    def append(self,value):
        self.data += value
x = MyString('hell ya')
print(x)
x.append(' oh shit')
print(x)