class MyClass1:
    def __init__(self):
        print("Default constructor called in MyClass1")

class MyClass2:
    def __init__(self, arg1):
        self.arg1 = arg1
        print("One argument constructor called with argument:", arg1, "in MyClass2")

class MyClass3:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        print("Two argument constructor called with arguments:", arg1, "and", arg2, "in MyClass3")

if __name__ == "__main__":
    obj1 = MyClass1()
    obj2 = MyClass2("Hello")
    obj3 = MyClass3("Hi", "there")
