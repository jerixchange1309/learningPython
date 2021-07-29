class hero:

    __jumlahHero = 0

    def __init__(self, nama):
        self.__nama = nama
        hero.__jumlahHero +=1

    #method hanya untuk object
    def getTotalpahlawan(self):
        return hero.__jumlahHero
    
    #method ini tidak berlaku untuk object namun berlaku untuk class
    def getTotalpahlawan1():
        return hero.__jumlahHero
    
    #static method (decorator) menempel pada class
    @staticmethod
    def getTotalpahlawan2():
        return hero.__jumlahHero

    @classmethod
    def getTotalpahlawanclass(diisiclass):
        return diisiclass.__jumlahHero
    

saber = hero('gedang')
#print(hero.getTotalpahlawan()) akan eror
print(hero.getTotalpahlawan1())

asasin = hero('suparjo')
print(hero.getTotalpahlawan2()) #menggunakan static method

rider = hero('king rosi')
print(hero.getTotalpahlawanclass()) #menggunakan class method


        