"""
The Liskov Substitution Principle (LSP) is another one of the five SOLID principles of object-oriented design.
It states that objects of a superclass should be replaceable with objects of a subclass without affecting the
correctness of the program. This means that a subclass should be able to stand in for its parent class without
causing unexpected behavior.
"""

from abc import ABC, abstractmethod


# Base classes
class Bird(ABC):
    pass


class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass


class NonFlyingBird(Bird):
    pass


# Subclasses
class Sparrow(FlyingBird):
    def fly(self):
        return "Sparrow flying"


class Penguin(NonFlyingBird):
    pass


# Function to let the bird fly
def let_bird_fly(bird: FlyingBird):
    print(bird.fly())


# Instances
sparrow = Sparrow()
penguin = Penguin()

# Using the function
let_bird_fly(sparrow)  # Works fine
# let_bird_fly(penguin)  # Raises a type error, as expected
