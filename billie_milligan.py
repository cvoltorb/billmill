#usr/bin/env python3

class Hi:
    def __init__(self, messages=[]):
        self.messages = messages
        self.messages = ["Hi there! I'm Billie", 'What do You want?']
    
    def say_hi(self):
        for m in self.messages:
            print(m)

class Input:
    def __init__(self, per=None, thing='', keywords=[]):
        self.per = Person()
        self.thing = thing
        self.keywords = keywords
        self.keywords = [
            "call", "who", "no", "show all"
        ]

    def input(self, thing=''):
        self.thing = input()
        if self.thing in self.keywords:
            if self.thing == "call":
                print("Who do You want to call?")
                self.call(self)
                print("Anything else?")
                self.input(self)
            elif self.thing == "who":
                self.who(self)
                print("Anything else?")
                self.input(self)
            elif self.thing == "show all":
                print(list(Person().persons))
                print("Anything else?")
                self.input(self)
            elif self.thing == "no":
                print("Okay")
        else:
            print("I don't know what You mean")
            self.input(self)
            
    def call(self, per):
        self.per.call()

    def who(self, per):
        self.per.who()

class Personality:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def describe(self):
        print("Hi, this is {0}, I'm {1} years old".format(self.name, self.age))

    def who(self):
        print("It's me, {0}!".format(self.name))
   
class Billie(Personality):
    def __init__(self):
        name = "Billie"
        age = 28
        Personality.__init__(self, name, age)

class Arthur(Personality):
    def __init__(self):
        name = "Arthur"
        age = 37
        Personality.__init__(self, name, age)

class Annie(Personality):
    def __init__(self):
        name = "Annie"
        age = 7
        Personality.__init__(self, name, age)

class Mike(Personality):
    def __init__(self):
        name = "Mike"
        age = 21
        Personality.__init__(self, name, age)

class Christopher(Personality):
    def __init__(self):
        name = "Christopher"
        age = 18
        Personality.__init__(self, name, age)

class Donna(Personality):
    def __init__(self):
        name = "Donna"
        age = 24
        Personality.__init__(self, name, age)

class Betty(Personality):
    def __init__(self):
        name = "Betty"
        age = 41
        Personality.__init__(self, name, age)

class Person:
    def __init__(self, inp='', persons={}, person=Billie()):
        self.inp = inp
        self.person = person
        self.persons = persons
        self.persons = {
            'billie': Billie(),
            'arthur': Arthur(),
            'annie': Annie(),
            'mike': Mike(),
            'chris': Christopher(),
            'donna': Donna(),
            'betty': Betty()
        }

    def call(self):
        self.inp = input()
        if self.inp in self.persons:
            self.person = self.persons[self.inp]
            self.describe()
        else:
            print("There is no {0} here".format(self.inp))

    def describe(self):
        if not type(self.person) == str:
            self.person.describe()
        else:
            print("And there is no description for that!")
        
    def who(self):
        if not type(self.person) == str:
            self.person.who()
        else:
            print("I'm Billie!")
    
hi = Hi()
hi.say_hi()

inp = Input()
inp.input()