from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def abstract_method(self):
        pass

    def non_abstract_method(self):
        print(f"This is a non-abstract method with value: {self.value}")

class SubClass(AbstractClassExample):
    def __init__(self, value):
        super().__init__(value)

    def abstract_method(self):
        print(f"Implementation of the abstract method with value: {self.value}")

if __name__ == "__main__":
    obj = SubClass(42)
    obj.abstract_method()
    obj.non_abstract_method()
