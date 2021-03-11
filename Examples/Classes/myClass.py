# A simple example of defining a class in Python.
class myClass:
    name = "My Object" # Luokan jäsenmuuttuja

    # Function specified in class is called a member variable or a method
    def printName(self): # Parameter 'self' refers to the object itself
        print(self.name)

object1 = myClass()
object2 = myClass()

object1.name = "The best object there is"

object1.printName() # Instead of print(object1.name)
object2.printName()
