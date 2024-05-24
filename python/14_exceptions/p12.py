try:
    class MyClass:
        pass

    obj = MyClass()
    print(obj.non_existent_field)
except AttributeError:
    print("Attribute not found.")
