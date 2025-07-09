# practice on generator (func->yield) vs iterator

def generator():
    while value < 10:
        yield value
        value += 1

class iterator:
    def _init_(self, max = 0):
        self.n = 0
        self.max = max

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        
        result = 2 ** self.n
        self.n += 1
        return result
    
def generator_func():
    n = 0
    while n < 50000:
        yield n
        n += 1

gen = generator_func()
print(next(gen))
print(next(gen), "\n")

# decorators

def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after\n")
    return wrapper

@decorator
def func():
    print("inside")

func()

# class, obj, constructor, inheratance

class car:
    # default constructor
    def __init__ (self):
        self.name = "Toyota"
        self.model = "Corolla"

    # parameterized constructor
    def __init__ (self, name, model):
        self.name = name
        self.model = model
    
    def display(self):
        print(self.name, "\n")

# make an object and call parameterized constructor
Car = car("Vitz", "2020")

# object properties are editable
Car.name = "Honda"

# del Car.name  # delete property
# Car.display() # wont work now since name is deleted

del Car  # delete object

# child class inherits 'car' parent class
class vehicle(car):
    # an init function can be created in child class
    # it can either override the parent class constructor
    # or call the parent class constructor (using super or the parent class name)
    # def __init__(self, name, model):
    #     super().__init__(name, model)
    pass

Vehicle = vehicle("Honda", "2021") # calls parent class constructor
Vehicle.display()  # calls parent class method

# what is the use of __new__?
# why use super?

# @classmethod, @staticmethod, @property

class student:
    # instance method
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    # operates on the class rather than an instance
    @classmethod
    def from_string(cls, string):
        name, rollno = string.split("-")
        return cls(name, rollno)
    
    # a utility function that does not depend on class or instance
    @staticmethod
    def add(x,y):
        return x + y
    
    # property decorator essentially acts as a getter
    @property
    def name(self):
        return self._name
    
    # setter
    @name.setter
    def name(self, n):
        self._name = n
    
    # deleter
    @name.deleter
    def name(self):
        del self._name
    
    # the above are called implicitly
    # setter can be used for validation