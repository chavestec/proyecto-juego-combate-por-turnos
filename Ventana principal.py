import funcionabout 
import tkinter as tk
import Ventanabatallas
from PIL import Image, ImageTk
window=tk.Tk()
window.geometry('700x700')
window.title('Las Aventuras del estudiante')


about = tk.Button(window,text=('About'),font=('Papyrus',12),command=funcionabout.botonabout)
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

        


supphoto=supphoto=tk.PhotoImage(file='Supphoto.png')
batphoto=tk.PhotoImage(file='Batphoto.png')
wophoto=tk.PhotoImage(file='Wonderphoto.png')
flashphoto=tk.PhotoImage(file='Flashphoto.png')


x=tk.IntVar()

Supbox=tk.Checkbutton(window,text='Superman ',variable=x, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='blue',
                        activeforeground='red', activebackground='black', image=supphoto, compound = 'right')
Wobox=tk.Checkbutton(window,text='Wonder Woman ',variable=x, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='blue',
                        activeforeground='red', activebackground='black', image=wophoto, compound = 'right')
Batbox=tk.Checkbutton(window,text='Batman ',variable=x, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='blue',
                        activeforeground='red', activebackground='black', image=batphoto, compound = 'right')
Flashbox=tk.Checkbutton(window,text='Flash ',variable=x, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='blue',
                        activeforeground='red', activebackground='black', image=flashphoto, compound = 'right')
Supbox.pack()
Batbox.pack()
Flashbox.pack()
Wobox.pack()


def paginabatalla():
    if (x.get())==1 and (usuario.get()!=''):
        window.destroy()
        Ventanabatallas.principalis()
        
    elif(x.get())==0:
        recordatorio=tk.Label(window,text=('DEBE SELECCIONAR UN PERSONAJE'), font=('Papyrus',12,'bold'))
        recordatorio.pack()

        
iniciar=tk.Button(window, text='Iniciar', font=('Papyrus',12),command=paginabatalla)

iniciar.pack()



window.mainloop()


