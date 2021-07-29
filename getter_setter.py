class hero:
    def __init__(self,name,healt,armor):
        self.name = name
        self.__healt = healt
        self.__armor = armor
        #self.info = 'name {} : \n\thealt: {}'.format(self.name,self.__healt)

    @property
    def info(self):
        return "name {} : \n\thealt: {}".format(self.name,self.__healt)
    
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor

    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        print('deleter nya armor')
        self.__armor = None

arcer = hero('contoh',29,30)

print('merubah info')
print(arcer.info)
arcer.name = 'suparjo'
print(arcer.info)

print('untuk getter dan setter __armor')
print(arcer.info)
arcer.armor = 69
print(arcer.armor)

print('deleter nya armor')
del arcer.armor
print(arcer.__dict__)