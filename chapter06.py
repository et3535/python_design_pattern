#Observer Pattern pull or push method
#subject와 observer 객체를 연결 , subject 변경시에 연결되어 있는 observer 객체 method를 실행하여 데이터 전달

class Subject:
    def __init__(self):
        self.__observers=[]
    
    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)

class Observer1:
    def __init__(self, subject):
        subject.register(self)
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'Form', subject)

class Observer2:
    def __init__(self, subject):
        subject.register(self)
    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'Form', subject)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)

subject.notifyAll('Notification')

