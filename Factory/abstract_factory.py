'''
The Abstract Factory pattern is a creational design pattern that provides an interface for creating families of related
or dependent objects without specifying their concrete classes. This pattern is useful when a system needs to be
independent of how its products are created or represented and when it needs to support multiple families of products.
'''

from abc import ABC, abstractmethod

# Abstract Products
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Concrete Products
class WindowsButton(Button):
    def paint(self):
        return "Windows Button"

class MacOSButton(Button):
    def paint(self):
        return "macOS Button"

class WindowsCheckbox(Checkbox):
    def paint(self):
        return "Windows Checkbox"

class MacOSCheckbox(Checkbox):
    def paint(self):
        return "macOS Checkbox"

# Abstract Factory
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Concrete Factories
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

class MacOSFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacOSButton()

    def create_checkbox(self) -> Checkbox:
        return MacOSCheckbox()

# Client Code
def client_code(factory: GUIFactory):
    button = factory.create_button()
    checkbox = factory.create_checkbox()
    print(button.paint())
    print(checkbox.paint())

# Testing client code with different factories
print("Client: Testing with WindowsFactory:")
client_code(WindowsFactory())

print("\nClient: Testing with MacOSFactory:")
client_code(MacOSFactory())
