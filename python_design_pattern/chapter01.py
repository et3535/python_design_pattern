# B inherit A
# B use A function

class A:
    def a1(self):
        print("A1")

class B(A):
    def b(self):
        print("B1")

b = B()
b.a1()

# Abstraction

class Adder:
    def __init__(self):
        self.sum =0
    def add(self,value):
        self.sum+=value

acc = Adder()
for i in range(99):
    acc.add(i)

print(acc.sum)

#Composition (object + object + function .....)
class A2(object):
    def a1(self):
        print("A")

class B2(object):
    def b(self):
        print("B2")
        A().a1()

objectB = B2()
objectB.b()


#Design is solving of problem


#Design is three pattern
#patterns is singletone, adapter and observer



