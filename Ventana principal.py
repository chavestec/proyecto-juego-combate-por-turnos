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

        


supphoto_original=Image.open('Supphoto.png')
batphoto_original=Image.open('Batphoto.png')
wophoto_original=Image.open('Wonderphoto.png')
flashphoto_original=Image.open('Flashphoto.png')

supphoto_resize=supphoto_original.resize((100,100))
supphoto=ImageTk.PhotoImage(supphoto_resize)

batphoto_resize=batphoto_original.resize((100,100))
batphoto=ImageTk.PhotoImage(batphoto_resize)

wophoto_resize=wophoto_original.resize((100,100))
wophoto=ImageTk.PhotoImage(wophoto_resize)

flashphoto_resize=flashphoto_original.resize((100,100))
flashphoto=ImageTk.PhotoImage(flashphoto_resize)

s=tk.IntVar()
b=tk.IntVar()
w=tk.IntVar()
f=tk.IntVar()

Supbox=tk.Checkbutton(window,text='Superman ',variable=s, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='blue',width=175,height=100, 
                        activeforeground='red', activebackground='black', image=supphoto, compound = 'right')
Wobox=tk.Checkbutton(window,text='Wonder Woman ',variable=w, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='blue',width=220,height=100,
                        activeforeground='red', activebackground='black', image=wophoto, compound = 'right')
Batbox=tk.Checkbutton(window,text='Batman ',variable=b, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='blue',width=175,height=100,
                        activeforeground='red', activebackground='black', image=batphoto, compound = 'right')
Flashbox=tk.Checkbutton(window,text='Flash ',variable=f, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='blue',width=175,height=100,
                        activeforeground='red', activebackground='black', image=flashphoto, compound = 'right')
Supbox.place(x=10, y=300)
Wobox.place(x=220,y=300)
Batbox.place(x=10, y=415)
Flashbox.place(x=220, y=415)

def paginabatalla():
    if (s.get())+(w.get())+(b.get())+(f.get())==3 and (usuario.get()!=''):
        window.destroy()
        Ventanabatallas.principalis()
        
    elif(s.get())+(w.get())+(b.get())+(f.get())!=3:
        recordatorio=tk.Label(window,text=('DEBE SELECCIONAR TRES PERSONAJE'), font=('Papyrus',12,'bold'))
        recordatorio.pack()

        
iniciar=tk.Button(window, text='Iniciar', font=('Papyrus',12),command=paginabatalla)

iniciar.pack()



window.mainloop()


