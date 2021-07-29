#membuat semua action sama
from abc import ABC, abstractmethod

class Button(ABC):

    #memasukan dekorator
    @abstractmethod
    def click(self):
        pass

class PushButton(Button):
    def click(self):
        print("ini push button dengan abstrack class")

tombolPush = PushButton()

tombolPush.click()
help(tombolPush)