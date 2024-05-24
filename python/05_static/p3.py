class my_class:
    static_variable="Hello world"

obj=my_class()
obj.static_variable="Hello Ankur"
print(my_class.static_variable)
print(obj.static_variable)