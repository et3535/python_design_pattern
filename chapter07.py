# Command Pattern
class Wizard():
    def __init__(self,src,rootdir):
        self.choice = []
        self.rootdir = rootdir
        self.src = src
    def preference(self, command):
        self.choice.append(command)

    def execute(self):
        for choice in self.choice:
            print(choice)   #{'python': True}
            print(choice.values()) # dict_values([True])
            print(list(choice.values())[0]) # True or False
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, "to", self.rootdir)
            else:
                print("No Operation")

if __name__=='__main__':
    wizard = Wizard('python3.5.gzip','/usr/bin/')
    wizard.preference({'python':True})
    wizard.preference({'java':False})
    wizard.execute()


# Second Example

from abc import ABCMeta, abstractmethod
class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class BuyStockOrder(Order):
    def __init__(self,stock):
        self.stock = stock
    def execute(self):
        self.stock.buy()

class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock
    
    def execute(self):
        self.stock.sell()


class StockTrade:
    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stock")

class Agent:
    def __init__(self):
        self.__orderQueue=[]

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        order.execute()

if __name__=='__main__':
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)