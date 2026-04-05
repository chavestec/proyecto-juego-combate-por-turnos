
import tkinter as tk
window=tk.Tk()
window.geometry('700x700')
window.title('Las Aventuras del estudiante')


def botonabout():
    venab=tk.Tk()
    venab.geometry('800x600')
    venab.title('Sobre este juego')
    info=tk.Label(venab,text=('Informacion Importante'), font= ('Arial',12))
    info.pack()
    venab.mainloop()
about = tk.Button(window,text=('About'),font=('Papyrus',12),command=botonabout)
about.pack()



instruccion=tk.Label(window,text=('Introduzca su nombre'), font=('Papyrus',12,'bold'))
instruccion.pack()
def prograbotonuser():
    user=usuario.get()
    bienvenido.config(text=('Bienvenido'), font=('Papyrus',18))
    usuariovisible.config(text=user,font=('Papyrus',18))
    
botonuser=tk.Button(window,text=('Aceptar'), font=('Papyrus',12),command=prograbotonuser)

usuario = tk.Entry()
usuario.config(font=('Papyrus',12))
usuario.pack()
botonuser.pack()
usuariovisible=tk.Label(window)

bienvenido=tk.Label(window)
bienvenido.pack()
usuariovisible.pack()
window.mainloop()
