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

    def call_non_abstract_method(self):
        # Create an instance of the SubClass and call the non-abstract method
        sub_obj = SubClass(self.value)
        sub_obj.non_abstract_method()

if __name__ == "__main__":
    obj = SubClass(42)
    obj.call_non_abstract_method()
