#marai bingung cok

class A:
    def show(self):
        print('ini a')

class B(A):
    def show(self):
        print('ini b')

class C(A):
    def show(self):
        print('ini c')
    
class D(B,C):
    pass

objek = D()
objek.show()
