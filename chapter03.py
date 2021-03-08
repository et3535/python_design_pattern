#Factory Pattern
#Other class create

#1. simple factory pattern
from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def do_say(self):
        pass

class Dog(Animal):
    def do_say(self):
        print("Bhow Bhow")

class Cat(Animal):
    def do_say(self):
        print("Meow Meow!")

## forest factory definition
class ForestFactory(object):
    def make_sound(self, object_type):
        return eval(object_type)().do_say()

if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("DOG or CAT")
    ff.make_sound(animal)        


# Factory Method Pattern
class Section(metaclass=ABCMeta):
    @abstractmethod
    def describe(self):
        pass

class PersonalSection(Section):
    def describe(self):
        print("PersonalSection")

class AlbumSection(Section):
    def describe(self):
        print("AlbumSection")

class PatentSection(Section):
    def describe(self):
        print("PatentSection")

class PublicationSection(Section):
    def describe(self):
        print("PublicationSection")


class Profile(metaclass=ABCMeta):
    def __init__(self):
        self.section = []
        self.createProfile()
    
    @abstractmethod
    def createProfile(self):
        pass

    def getSection(self):
        return self.section

    def addSection(self,section):
        self.section.append(section)


class linkedin(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(PatentSection())
        self.addSection(PublicationSection())

class facebook(Profile):
    def createProfile(self):
        self.addSection(PersonalSection())
        self.addSection(AlbumSection())

if __name__=='__main__':
    profile_type = input("linkedin or facebook")
    profile = eval(profile_type.lower())()
    print("Profile has section --", profile.getSection())

#Abstract Factory Pattern
