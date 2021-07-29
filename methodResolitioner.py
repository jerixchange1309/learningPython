#method resolutioner adalah pembacaan method secara multiple inheritance
#pembacaan multiple nya adalah dia yang paling awal di panggil dalam suatu class

class A:
    def show(self):
        print('ealah ini a')
    
class B:
    def show(self):
        print('ealah ini b')

class gabungan(B,A):
    pass

objek = gabungan()
objek.show()