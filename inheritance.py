#inheritance adalah sub class

class makanan:
    def __init__(self,nama_makanan,daerah):
        self.daerah = daerah
        self.makanan = nama_makanan
    
class makanan_manis(makanan):
    pass
class makanan_gurih(makanan):
    pass

nasi_padang = makanan('nasi padang','padang') #makanan merupakan supperclass
gethuk = makanan_manis('gethuk','bantul') #makanan_manis merupakan sub class

print(gethuk.daerah)
print(nasi_padang.daerah)

print(gethuk.__dict__)