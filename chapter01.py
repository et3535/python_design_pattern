# B는 A를 상속 받는다.
# B는 A의 function을 사용 할 수 있다.

class A:
    def a1(self):
        print("A1")

class B(A):
    def b(self):
        print("B1")

b = B()
b.a1()


# 추상화 (Abstraction) 

class Adder:
    def __init__(self):
        self.sum =0
    def add(self,value):
        self.sum+=value

acc = Adder()
for i in range(99):
    acc.add(i)

print(acc.sum)

#Composition 객체와 객체를 연결하여 사용 (object + object + function .....)
class A2(object):
    def a1(self):
        print("A")

class B2(object):
    def b(self):
        print("B2")
        A().a1()

objectB = B2()
objectB.b()


#디자인 패턴은 문제를 해결하는데 사용한다.
#디자인 패턴은 크게 3가지로 볼 수 있다. (singletone, adapter and observer)



