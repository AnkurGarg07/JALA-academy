from p2_module1 import MyClass

class SubClass(MyClass):
    def access_protected_members(self):
        print(self._protected_variable)
        self._protected_method()

if __name__ == "__main__":
    sub_obj = SubClass()
    sub_obj.access_protected_members()
