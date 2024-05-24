from p3_module1 import MyClass

class DifferentModuleClass:
    def access_public_members(self):
        obj = MyClass()
        print(obj.public_variable)
        obj.public_method()

if __name__ == "__main__":
    different_module_obj = DifferentModuleClass()
    different_module_obj.access_public_members()