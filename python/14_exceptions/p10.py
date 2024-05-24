try:
    class MyClass:
        pass
    obj = MyClass()
    print(obj.undefined_attribute)
except AttributeError:
    print("Attribute not found.")
