class hero:
    #class variable
    jumlah = 0

    def __init__(self, inputName, inputPower, inputHealt):
        #instance variable
        self.name = inputName
        self.power = inputPower
        self.healt = inputHealt

        hero.jumlah += 1

    #void function, method tanpa return tanpa variable
    def siapa(self):
        print('nama hero ' + self.name)
    
    #method dengan argument, tanpa return
    def healtUp(self,up):
        self.healt += up

    #method dengan return
    def getHealt(self):
        return self.healt

hero1 = hero('parjono',100,30)
hero2 = hero('suparman',200,10)

hero1.siapa()
hero1.healtUp(20)

print(hero1.getHealt())

        
        
        