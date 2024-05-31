"""
The Interface Segregation Principle (ISP) is one of the five SOLID principles of object-oriented design.
It states that no client should be forced to depend on methods it does not use. In other words,
it's better to have many specific interfaces rather than a single, general-purpose interface.
This helps to reduce the impact of changes and makes the system more flexible and easier to maintain.
"""

from abc import ABC, abstractmethod


# Interfaces
class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass


# Implementations
class HumanWorker(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")


class RobotWorker(Workable):
    def work(self):
        print("Robot working")


# Functions using the interfaces
def perform_work(worker: Workable):
    worker.work()


def perform_eat(worker: Eatable):
    worker.eat()


def perform_sleep(worker: Sleepable):
    worker.sleep()


# Instances
human = HumanWorker()
robot = RobotWorker()

# Using the functions
perform_work(human)
perform_work(robot)

perform_eat(human)
# perform_eat(robot)  # This will raise an error, as expected

perform_sleep(human)
# perform_sleep(robot)  # This will raise an error, as expected
