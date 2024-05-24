class MyClass:
    def __init__(self):
        self.__private_field = "I am private"

    def __private_method(self):
        print("This is a private method")

    def access_private(self):
        # Public method to access private field and method
        print(self.__private_field)
        self.__private_method()

    @staticmethod
    def main():
        obj = MyClass()
        obj.access_private()
class subClass(MyClass):
    def try_access_private(self):
        try:
            print(self.__private_field)  #Error
        except AttributeError as e:
            print(f"Error: {e}")

        try:
            self.__private_method()  #Error
        except AttributeError as e:
            print(f"Error: {e}")

        # Accessing private field and method via public method
        self.access_private()
if __name__ == "__main__":
    MyClass.main()

    # Create an instance of SubClass
    sub_obj = subClass()
    
    # Attempt to access private fields and methods
    print("\nAttempting to access private fields and methods from subclass:")
    sub_obj.try_access_private()

