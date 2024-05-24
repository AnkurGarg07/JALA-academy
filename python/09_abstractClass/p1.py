from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print(f"This is a non-abstract method with value: {self.value}")

