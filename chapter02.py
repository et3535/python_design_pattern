#singleton pattern 을 작성해본다.
#하나의 객체를 생성해서 공용으로 사용하는 디자인 패턴이다.

class Singleton(object):
    def __new__(cls):
        if not hasattr(cls,'instance'):
            print("not hasattr")
            cls.instance = super(Singleton,cls).__new__(cls)
        print("if exit")
        return cls.instance

s = Singleton()
print("object created", s)

s1 = Singleton()
print("object created",s1)


class Singleton2:
    __instance=None
    def __init__(self):
        if not Singleton2.__instance:
            print(" __init__ method called")
        else:
            print("Instance already created :", self.getInstance())
    
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton2()
        return cls.__instance

s = Singleton2()
print("object created", Singleton2().getInstance())
s1 = Singleton2()

#Database Singleton 패턴으로 작성한 내용이다.
import sqlite3
class MetaSingleton(type):
    _instance = {}
    def __call__(cls,*args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls]= super(MetaSingleton,cls).__call__(*args,**kwargs)
        return cls._instance[cls]

class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect("db.sqlite3")
            self.cursorobj = self.connection.cursor()
        return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print("Database Object Db1",db1)
print("Database Object Db2",db2)


#서버 상태를 체크하는 코드다.

class HealthCheck:
    _instance = None
    def __new__(cls,*args,**kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck,cls).__new__(cls,*args,**kwargs)
        return HealthCheck._instance
    def __init__(self):
        self._server = []
    def addServer(self):
        self._server.append("SERVER1")
        self._server.append("SERVER2")
        self._server.append("SERVER3")
        self._server.append("SERVER4") 
    def changeServer(self):
        self._server.pop()
        self._server.append("SERVER5")

hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("Schedule health check for server (1)...")
for i in range(4):
    print("checking ",hc1._server[i])

hc2.changeServer()
print("Schedule health check for server (2)...")
for i in range(4):
        print("checking ",hc2._server[i])