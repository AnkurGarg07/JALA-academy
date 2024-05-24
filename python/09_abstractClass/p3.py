from abc import ABC, abstractmethod

class AbstractClassExample(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class SubClass(AbstractClassExample):
    def __init__(self):
        super().__init__()

    def abstract_method(self):
        print("Implementation of the abstract method in SubClass")

    def call_abstract_method(self):
        # Create an instance of the SubClass and call the abstract method
        sub_obj = SubClass()
        sub_obj.abstract_method()

if __name__ == "__main__":
    obj = SubClass()
    obj.call_abstract_method()
