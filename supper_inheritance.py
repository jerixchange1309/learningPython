class hero:
    def __init__(self,name,healt):
        self.name = name
        self.healt = healt

    def showInfo(self):
        print("{} dengan healt {}".format(self.name,self.healt))
    
class hero_baik(hero):
    def __init__(self,name):
        super().__init__(name, 100)
    
    #override
    def overideInfo(self):
        print("{} dengan healt {}".format(self.name,self.healt))

class hero_jahat(hero):
    def __init__(self,name):
        super().__init__(name,200)
        super().showInfo()

jahat = hero_jahat('penjahat')
baik = hero_baik('pembaik')

jahat.showInfo()
baik.overideInfo()
