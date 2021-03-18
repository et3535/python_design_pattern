#상태 패턴 : 상태를 서브 클래스로 만들고, 추상화 클래스로 행위를 작성
from abc import abstractmethod,ABCMeta

class State(metaclass=ABCMeta):
    @abstractmethod
    def doThis(self):
        pass

class StartState(State):
    def doThis(self):
        print("TV Switching ON..")

class StopState(State):
    def doThis(self):
        print("TV Switching OFF..")


class TVContext(State):
    def __init__(self):
        self.state=None
    def getState(self):
        return self.state
    
    def setState(self,state):
        self.state=state

    def doThis(self):
        self.state.doThis()

context = TVContext()
context.getState()

start = StartState()
stop  = StopState()

context.setState(start)
context.doThis()
context.setState(stop)
context.doThis()