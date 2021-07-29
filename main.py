class hero:
     
    def __init__(self, heroName, heroHealt, heroPower, heroArmor):
        self.name = heroName
        self.healt = heroHealt
        self.power = heroPower
        self.armor = heroArmor
    
    def menyerang(self, lawan):
        print(self.name + ' menyerang ' + lawan.name)
        lawan.diserang(self, self.power)
    
    def diserang(self, lawan, powerLawan):
        print(self.name + ' diserang ' + lawan.name)
        attack_diserang = powerLawan/self.armor
        print('serangan dari lawan ' + str(self.healt))
        self.healt -= attack_diserang
        print(self.name + ' diserang oleh ' + lawan +  str(self.healt))


saber = hero('arthur',200,10,50)
archer = hero('gilgamesh',100,20,10)

saber.menyerang(archer)
        