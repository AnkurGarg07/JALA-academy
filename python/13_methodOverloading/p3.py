class MyClass:

    def my_method(self, a,b):
        return a+b
    def my_method(self,a,b):
        return a*b


if __name__ == "__main__":
    obj = MyClass()
    print(obj.my_method(1, 2))
    print(obj.my_method(1,2))
