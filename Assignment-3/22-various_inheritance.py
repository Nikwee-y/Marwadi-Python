# Enrollment No: 92600565001

class A:
    def show(self):
        print("class A")

class B(A):
    pass

class C(A):
    pass

class D(B,C):
    pass

D().show()