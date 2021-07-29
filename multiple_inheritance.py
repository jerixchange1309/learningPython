class Minuman:
    def setMinuman(self,nama_minuman):
        self.meminum = nama_minuman
    
    def showMinuman(self):
        print(self.meminum)

class Makanan:
    def setMakanan(self,nama_makanan):
        self.memakan = nama_makanan

    def showMakanan(self):
        print(self.memakan)

class Warteg(Minuman,Makanan):
    def __init__(self,makanapa,minumapa):
        self.makanapa = makanapa
        self.minumapa = minumapa
    
marjiono = Warteg('mendoan','es jahe')
marjiono.setMinuman('wedang ronde')
marjiono.setMakanan('nasi kucing')

marjiono.showMakanan()
marjiono.showMinuman()

print(marjiono.__dict__)