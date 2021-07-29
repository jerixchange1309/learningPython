class hero:
    
    def __init__(self, name, attack, healt):
        self.__name = name
        self.__attack = attack
        self.__healt = healt

    #getter

    def getName(self):
        return self.__name
    
    def getHealt(self):
        return self.__healt
    
    #setter
    def diserang(self,damage):
        self.__healt -= damage

#awal game

archer = hero('emiya kiritsugu',100,200)
saber = hero('arthuria', 200,200)

#game berjalan

print(saber.__dict__)
print(saber.getHealt())
saber.diserang(19)
print(saber.getHealt())

         