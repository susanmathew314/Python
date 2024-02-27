

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


class Cow(Animal):
    def speak(self):
        return f"{self.name} says Moo!"


# Creating instances of subclasses
dog = Dog("Buddy")
cat = Cat("Whiskers")
cow = Cow("Bessie")

# Calling speak method on each instance
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!
print(cow.speak())  # Output: Bessie says Moo!
