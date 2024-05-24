from p2_module1 import MyClass

class NonSubClass:
    def access_protected_members(self):
        obj = MyClass()
        try:
            print(obj._protected_variable)
        except AttributeError as e:
            print(f"Error: {e}")
        
        try:
            obj._protected_method()
        except AttributeError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    non_sub_obj = NonSubClass()
    non_sub_obj.access_protected_members()
