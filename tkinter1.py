import tkinter
from typing import Text

main_window = tkinter.Tk()

contohLabel1 = tkinter.Label(main_window, text='ini label')
contohBtn1 = tkinter.Button(main_window, text='ini button')

#method positioning
contohLabel1.pack()
contohBtn1.pack()
#method menampilkan gui
main_window.mainloop()