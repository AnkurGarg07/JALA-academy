
class A:
    def method_a1(self):
        print("Method A1 in class A")
    
    def method_a2(self):
        print("Method A2 in class A")
    
    # Overridden method
    def common_method(self):
        print("Common method in class A")


class B(A):
    
    def method_b1(self):
        print("Method B1 in class B")
    
    
    def method_b2(self):
        print("Method B2 in class B")
    
    # Overridden method
    def common_method(self):
        print("Common method in class B")

class C(B):

    def method_c1(self):
        print("Method C1 in class C")
    
    
    def method_c2(self):
        print("Method C2 in class C")
    
    # Overridden method
    def common_method(self):
        print("Common method in class C")

def main():
    a = A()
    print("Calling methods of class A:")
    a.method_a1()
    a.method_a2()
    a.common_method()

    b = B()
    print("\nCalling methods of class B:")
    b.method_b1()
    b.method_b2()
    b.common_method()

    c = C()
    print("\nCalling methods of class C:")
    c.method_c1()
    c.method_c2()
    c.common_method()
    

if __name__ == "__main__":
    main()
