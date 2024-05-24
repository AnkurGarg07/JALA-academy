class MyClass:
    def my_method(self, a,b):
        return a+b
    def my_method(self,a,b,c):
        return a+b+c

if __name__ == "__main__":
    obj = MyClass()
    print(obj.my_method(1, 2.8,3.5))
    print(obj.my_method(1,2))
