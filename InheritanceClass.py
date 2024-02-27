class A:
    def feature1(self):
        print('Feature 1 is working')
    def feature2(self):
        print('Feature 2 is working')
# Obj1=A()
# Obj1.feature1()
# Obj1.feature2()

class B(A):
    def feature3(self):
        print('Feature 3 is working')
    def feature4(self):
        print('Feature 4 is working')
# Obj1=B()
# Obj1.feature1()
# Obj1.feature2()
# Obj1.feature3()
# Obj1.feature4()

class C(B):
    def feature5(self):
        print('Feature 5 is working')
    def feature6(self):
        print('Feature 6 is working')
# Obj1=C()
# Obj1.feature1()
# Obj1.feature2()
# Obj1.feature3()
# Obj1.feature4()
# Obj1.feature5()
# Obj1.feature6()

class D(A,B,C):
    def __init__(self):
        super().__init__()
    def use_classes(self):
        self.A()
        self.B()
        self.C()


Obj1=D()
Obj1.use_classes()