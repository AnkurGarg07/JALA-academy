class MyClass:
    def __init__(self):
        self.public_variable = "I am public"
    
    def public_method(self):
        print("This is a public method")
    
    def show_details(self):
        print(self.public_variable)
        self.public_method()

class AnotherClass:
    def access_public_members(self):
        obj = MyClass()
        print(obj.public_variable)
        obj.public_method()

if __name__ == "__main__":
    another_obj = AnotherClass()
    another_obj.access_public_members()
