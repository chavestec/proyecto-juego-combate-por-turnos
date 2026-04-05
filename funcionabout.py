import tkinter as tk
n="En un lugar de la Mancha, de cuyo nombre no quiero acordarme, \nno hace mucho tiempo que vivía un hidalgo de los de lanza en \nastillero, adarga antigua, rocín flaco y galgo corredor"
def botonabout():
    venab=tk.Tk()
    venab.geometry('800x600')
    venab.title('Sobre este juego')
    info=tk.Label(venab,text=('Informacion Importante'), font= ('Arial',12))
    infor=tk.Label(venab,text= n, font= ('Arial',12))
    info.pack()
    infor.pack()
    venab.mainloop()

