## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## is-a
class Person(object):
    def __init__(self, name):
        ## has-a
        self.name = name

        ## Penson has-a pet of some kind
        self.pet = None

## is-a
class Employee(Person):

    def __init__(self, name, salary):
        ## has-a hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## has-a
        self.salary = salary

## is-a
class Fish(object):
    pass

## is-a
class Salmon(Fish):
    pass

## is-a
class Halibut(Fish):
    pass


## rover is-a Dog
rever = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## is-a
mary.pet = satan

## is-a
frank = Employee("Frank", 120000)

## is-a
frank.pet = rover

## is-a
flipper = Fish()

## is-a
crouse = Salmon()

## is-a
harry = Halibut()

