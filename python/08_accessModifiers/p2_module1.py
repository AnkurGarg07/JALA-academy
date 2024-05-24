class MyClass:
    def __init__(self):
        self._protected_variable = "I am protected"
    
    def _protected_method(self):
        print("This is a protected method")

    def public_method(self):
        print(self._protected_variable)
        self._protected_method()

class AnotherClass:
    def access_protected_members(self):
        obj = MyClass()
        print(obj._protected_variable)
        obj._protected_method()

if __name__ == "__main__":
    another_obj = AnotherClass()
    another_obj.access_protected_members()
