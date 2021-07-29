class hero: #template
    #class variable
    jumlah = 0
    
    def __init__(self, inputName, inputHealt, inputPower, inputArmor) -> None:
        self.name = inputName
        self.healt = inputHealt
        self.power = inputPower
        self.armor = inputArmor

        hero.jumlah += 1
        print('membuat hero dengan nama ', inputName)
        
hero1 = hero('suparjo',200,10,1)
print(hero.jumlah)
hero2 = hero('ceking',200,10,200)
print(hero.jumlah)
hero3 = hero('aku',1000,200,400)
print(hero.jumlah)

##dict akan mengambil semua data yang ada pada class
print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)

#print atribute
print(hero1.name)
print(hero2.healt)
print(hero3.power)


print('total hero ',hero.jumlah)