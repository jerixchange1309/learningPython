class hero:
    def __init__(self,name,healt,armor):
        self.name = name
        self.__healt = healt
        self.__armor = armor
        #self.info = 'name {} : \n\thealt: {}'.format(self.name,self.__healt)

    @property
    def info(self):
        return "name {} : \n\thealt: {}".format(self.name,self.__healt)

jajalan = hero('ini nama',20,20)
print(jajalan.info)

jajalan.name = "suparjo"
print(jajalan.info)