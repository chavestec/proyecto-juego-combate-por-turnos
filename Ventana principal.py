import funcionabout 
import tkinter as tk
from PIL import Image, ImageTk
#----------------VentanaBatallas-------------------------------------------------------------------------------------------------------------------------
def principalis():
    venjuego=tk.Tk()
    venjuego.geometry('1500x700')
    venjuego.resizable(False,False)
    venjuego.title('Batalla')
    info=tk.Label(venjuego,text=('Juego'), font= ('Arial',12))
    info.pack()
    supcarta=tk.Label(venjuego, text=('Aqui'),font= ('Arial',12))
    nosupcarta=tk.Label(venjuego, text=('Aqui no'))
    if (s.get())==1:
        supcarta=tk.Label(venjuego, text=('Superman'),font= ('Arial',12),fg='black')
        supcarta.pack()
    if (b.get())==1:
        batcarta=tk.Label(venjuego, text=('Batman'),font= ('Arial',12),fg='black')
        batcarta.pack()
    if (w.get())==1:
        Wondercarta=tk.Label(venjuego, text=('Wonder Woman'),font= ('Arial',12),fg='black')
        Wondercarta.pack()
    if (f.get())==1:
        flashcarta=tk.Label(venjuego, text=('Flash'),font= ('Arial',12),fg='black')
        flasharta.pack()      
    venjuego.mainloop()
#--------------------------------------------------------------------------------
#VentanaPrincipal
#----------------------------------------------------------------------------------------------
window=tk.Tk()
window.geometry('1500x700')
window.title('Las Aventuras del estudiante')
window.resizable(False,False)
fondo=tk.PhotoImage(file='fondo.png')
fondo=tk.Label(window,image=fondo)
fondo.place(relheight=1, relwidth=1, x=0, y=0 )

about = tk.Button(window,text=('About'),font=('Papyrus',12),command=funcionabout.botonabout)
about.pack()


instruccion=tk.Label(window,text=('Introduzca su nombre'), font=('Papyrus',12,'bold'))
instruccion.pack()
def prograbotonuser():
    user=usuario.get()
    if user!='':
        bienvenido.config(text=('Bienvenido'), font=('Papyrus',18))
        usuariovisible.config(text=user,font=('Papyrus',18))
    else:
        ''
    
    
botonuser=tk.Button(window,text=('Aceptar'), font=('Papyrus',12),command=prograbotonuser)

usuario = tk.Entry()
usuario.config(font=('Papyrus',12))
usuario.pack()
botonuser.pack()
usuariovisible=tk.Label(window)

bienvenido=tk.Label(window)
bienvenido.place(x=10,y=50)
usuariovisible.place(x=10, y=100)

        


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
    sumapersonajes=(s.get())+(w.get())+(b.get())+(f.get())
    if sumapersonajes==3:
        if (usuario.get()!=''):
            principalis()
        else:
            recordatorio=tk.Label(window,text=('DEBE ESCRIBIR SU NOMBRE, NOBLE JUGADOR'), font=('Papyrus',12,'bold'), bg='Black', fg='white')
            recordatorio.place(x=10,y=250)
            
        
    elif(s.get())+(w.get())+(b.get())+(f.get())!=3:
        recordatorio=tk.Label(window,text=('DEBE SELECCIONAR TRES PERSONAJES'), font=('Papyrus',12,'bold'))
        recordatorio.place(x=10,y=250)

        
iniciar=tk.Button(window, text='Iniciar', font=('Papyrus',12),command=paginabatalla)

iniciar.pack()
window.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------

        






