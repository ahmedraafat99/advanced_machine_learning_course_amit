class A():
    def do_this(self):
        print("in A")
class B(A):
     pass
class C():
    def do_this(self):
        print("in C")
class D(C,A):
    pass              
x=D()
x.do_this()