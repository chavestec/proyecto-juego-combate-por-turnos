import tkinter as tk
n=('Instituto Tecnológico de Costa Rica','\nEscuela de Computadores', '\nIntroducción a la programación', '\n2026', '\nGrupo 4', '\nPython 3.11.9','\nDescripción: Este programa es un proyecto que funciona como un juego de combate por turnos.  ')



def botonabout():
    venab=tk.Tk()
    venab.geometry('800x600')
    venab.title('Sobre este juego')
    info=tk.Label(venab,text=('Informacion Importante'), font= ('Arial',12))
    infor=tk.Label(venab,text= n, font= ('Arial',12))
    info.pack()
    infor.pack()
    venab.mainloop()

