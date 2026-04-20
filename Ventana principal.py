import funcionabout 
import tkinter as tk
from PIL import Image, ImageTk
#----------------VentanaBatallas-------------------------------------------------------------------------------------------------------------------------
def principalis():
    venjuego=tk.Tk()
    venjuego.geometry('1500x700')
    venjuego.resizable(False,False)
    venjuego.title('Batalla')
    def jugables():
        seleccion=tk.Canvas(venjuego, width=200, height=200)
        seleccion.pack()
        seleccionados=tk.Label(seleccion, text=('Personajes escogidos'))
        seleccionados.pack()
        if (s.get())==1:
            supcarta=tk.Label(seleccion, text=('Superman'),font= ('Arial',12),fg='black')
            supcarta.pack()
        elif (s.get())==0:
            supcarta=tk.Label(seleccion, text=('Superman malo'),font= ('Arial',12),fg='black')
            supcarta.pack()
        if (b.get())==1:
            batcarta=tk.Label(seleccion, text=('Batman'),font= ('Arial',12),fg='black')
            batcarta.pack()
        if (w.get())==1:
            Wondercarta=tk.Label(seleccion, text=('Wonder Woman'),font= ('Arial',12),fg='black')
            Wondercarta.pack()
        if (f.get())==1:
            flashcarta=tk.Label(seleccion, text=('Flash'),font= ('Arial',12),fg='black')
            flashcarta.pack()
        if (g.get())==1:
            greencarta=tk.Label(seleccion, text=('Green Lantern'),font= ('Arial',12),fg='black')
            greencarta.pack()
        if (h.get())==1:
            hawkcarta=tk.Label(seleccion, text=('Hawkgirl'),font= ('Arial',12),fg='black')
            hawkcarta.pack()
        if (mm.get())==1:
            martiancarta=tk.Label(seleccion, text=('Martian Manhunter'),font= ('Arial',12),fg='black')
            martiancarta.pack()
        if (ca.get())==1:
            canarycarta=tk.Label(seleccion, text=('Black Canary'),font= ('Arial',12),fg='black')
            canarycarta.pack()
        if (z.get())==1:
            zatannacarta=tk.Label(seleccion, text=('Zatanna'),font= ('Arial',12),fg='black')
            zatannacarta.pack()
        if (a.get())==1:
            arrowcarta=tk.Label(seleccion, text=('Green Arrow'),font= ('Arial',12),fg='black')
            arrowcarta.pack()
        if (bg.get())==1:
            goldcarta=tk.Label(seleccion, text=('Booster Gold'),font= ('Arial',12),fg='black')
            goldcarta.pack()
        if (m.get())==1:
            marvelcarta=tk.Label(seleccion, text=('Captain Marvel'),font= ('Arial',12),fg='black')
            marvelcarta.pack()
        if (nw.get())==1:
            marvelcarta=tk.Label(seleccion, text=('Nightwing'),font= ('Arial',12),fg='black')
            marvelcarta.pack()
        if (sg.get())==1:
            supgcarta=tk.Label(seleccion, text=('Supergirl'),font= ('Arial',12),fg='black')
            supgcarta.pack()
        if (aq.get())==1:
            aquacarta=tk.Label(seleccion, text=('Aquaman'),font= ('Arial',12),fg='black')
            aquacarta.pack()
    def villanos():
        seleccion=tk.Label(venjuegos, text=('Personajes villanos'))
        seleccion.pack()

    ubicaciones=['Patio Pricipal','Sala Entrenamiento','Salon Justicia','Puesto de vigilancia', 'Atalaya']
    
    def ubicacion_seleccionado():
        if (ub.get())==0:
            print('Opción 1')
        elif (ub.get())==1:
            print('Opción 2')
        elif (ub.get())==2:
            print('Opción 3')
    
    canvasmapa=tk.Canvas(venjuego,bg='grey')
    mapatitulo=tk.Label(canvasmapa, text=('Mapa'),font=('Papyrus',12))
    mapatitulo.pack()
    ub=tk.IntVar()
    for index in range(len(ubicaciones)):
        mapa=tk.Radiobutton(canvasmapa,text=ubicaciones[index],variable=ub,value=index,font=('Papyrus',12),
                                     command=ubicacion_seleccionado)
        mapa.pack(anchor='w')
    
    canvasmapa.place(x=0,y=0)
        
        
   
    info=tk.Label(venjuego,text=('Juego'), font= ('Arial',12))
    info.pack()
    return jugables()
    return villanos()
        
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
        usuariovisible.config(text= 'Super-'+user,font=('Papyrus',18))
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

#--------------------------------------------#Selecciondeavatar--------------------------------------------------------------------------------------------------
canvavatar=tk.Canvas(window)
textoavatar=tk.Label(window,text='Seleccione su avatar', font=('Papyrus',14))
textoavatar.place(x=1150, y=30)
opcionuno=Image.open('opcionuno.png')
avataruno=opcionuno.resize((50,50))
uno=ImageTk.PhotoImage(avataruno)

opciondos=Image.open('opcion2.png')
avatardos=opciondos.resize((50,50))
dos=ImageTk.PhotoImage(avatardos)

opciontres=Image.open('proteger.png')
avatartres=opciontres.resize((50,50))
tres=ImageTk.PhotoImage(avatartres)

def avatar_seleccionado():
    if (av.get())==0:
        print('Opción 1')
    elif (av.get())==1:
        print('Opción 2')
    elif (av.get())==2:
        print('Opción 3')
avatares=['Opción 1','Opción 2','Opción 3']
avataresimagenes=[uno,dos,tres]
av=tk.IntVar()
for index in range(len(avatares)):
    seleccionavatares=tk.Radiobutton(canvavatar,text=avatares[index],variable=av,value=index,font=('Papyrus',12),
                                     command=avatar_seleccionado,
                                     image=avataresimagenes[index])
    seleccionavatares.pack()
canvavatar.place(x=1200,y=70)


        


supphoto_original=Image.open('Supphoto.png')
batphoto_original=Image.open('Batphoto.png')
wophoto_original=Image.open('Wonderphoto.png')
flashphoto_original=Image.open('Flashphoto.png')
greenphoto_original=Image.open('greenphoto.png')
hawkphoto_original=Image.open('Hawkphoto.png')
martianphoto_original=Image.open('Martianphoto.png')
canaryphoto_original=Image.open('Canaryphoto.png')
zatannaphoto_original=Image.open('zatannaphoto.png')
arrowphoto_original=Image.open('arrowphoto.png')
goldphoto_original=Image.open('goldphoto.png')
marvelphoto_original=Image.open('marvelphoto.png')
nightphoto_original=Image.open('nightphoto.png')
supgphoto_original=Image.open('supgphoto.png')
aquaphoto_original=Image.open('aquaphoto.png')

supphoto_resize=supphoto_original.resize((100,100))
supphoto=ImageTk.PhotoImage(supphoto_resize)

supgphoto_resize=supgphoto_original.resize((100,100))
supgphoto=ImageTk.PhotoImage(supgphoto_resize)

aquaphoto_resize=aquaphoto_original.resize((100,100))
aquaphoto=ImageTk.PhotoImage(aquaphoto_resize)

nightphoto_resize=nightphoto_original.resize((100,100))
nightphoto=ImageTk.PhotoImage(nightphoto_resize)

arrowphoto_resize=arrowphoto_original.resize((100,100))
arrowphoto=ImageTk.PhotoImage(arrowphoto_resize)

goldphoto_resize=goldphoto_original.resize((100,100))
goldphoto=ImageTk.PhotoImage(goldphoto_resize)

martianphoto_resize=martianphoto_original.resize((100,100))
martianphoto=ImageTk.PhotoImage(martianphoto_resize)

zatannaphoto_resize=zatannaphoto_original.resize((100,100))
zatannaphoto=ImageTk.PhotoImage(zatannaphoto_resize)

batphoto_resize=batphoto_original.resize((100,100))
batphoto=ImageTk.PhotoImage(batphoto_resize)

wophoto_resize=wophoto_original.resize((100,100))
wophoto=ImageTk.PhotoImage(wophoto_resize)

flashphoto_resize=flashphoto_original.resize((100,100))
flashphoto=ImageTk.PhotoImage(flashphoto_resize)

greenphoto_resize=greenphoto_original.resize((100,100))
greenphoto=ImageTk.PhotoImage(greenphoto_resize)

hawkphoto_resize=hawkphoto_original.resize((100,100))
hawkphoto=ImageTk.PhotoImage(hawkphoto_resize)

canaryphoto_resize=canaryphoto_original.resize((100,100))
canaryphoto=ImageTk.PhotoImage(canaryphoto_resize)

marvelphoto_resize=marvelphoto_original.resize((100,100))
marvelphoto=ImageTk.PhotoImage(marvelphoto_resize)

s=tk.IntVar()
b=tk.IntVar()
w=tk.IntVar()
f=tk.IntVar()
g=tk.IntVar()
h=tk.IntVar()
mm=tk.IntVar()
ca=tk.IntVar()
z=tk.IntVar()
a=tk.IntVar()
bg=tk.IntVar()
m=tk.IntVar()
nw=tk.IntVar()
sg=tk.IntVar()
aq=tk.IntVar()

Supbox=tk.Checkbutton(window,text='Superman ',variable=s, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=175,height=100, 
                        activeforeground='red', activebackground='black', image=supphoto, compound = 'right')
Wobox=tk.Checkbutton(window,text='Wonder Woman ',variable=w, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=220,height=100,
                        activeforeground='red', activebackground='black', image=wophoto, compound = 'right')
Batbox=tk.Checkbutton(window,text='Batman ',variable=b, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=175,height=100,
                        activeforeground='red', activebackground='black', image=batphoto, compound = 'right')
Flashbox=tk.Checkbutton(window,text='Flash ',variable=f, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=175,height=100,
                        activeforeground='red', activebackground='black', image=flashphoto, compound = 'right')
Greenbox=tk.Checkbutton(window,text='Green Lantern ',variable=g, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=210,height=100,
                        activeforeground='red', activebackground='black', image=greenphoto, compound = 'right')
Hawkbox=tk.Checkbutton(window,text='Hawkgirl ',variable=h, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=175,height=100,
                        activeforeground='red', activebackground='black', image=hawkphoto, compound = 'right')
Martianbox=tk.Checkbutton(window,text='Martian Manhunter ',variable=mm, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=230,height=100,
                        activeforeground='red', activebackground='black', image=martianphoto, compound = 'right')
Canarybox=tk.Checkbutton(window,text='Black Canary ',variable=ca, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=205,height=100,
                        activeforeground='red', activebackground='black', image=canaryphoto, compound = 'right')
Zatannabox=tk.Checkbutton(window,text='Zatanna ',variable=z, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=175,height=100,
                        activeforeground='red', activebackground='black', image=zatannaphoto, compound = 'right')
Arrowbox=tk.Checkbutton(window,text='Green Arrow ',variable=a, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=190,height=100,
                        activeforeground='red', activebackground='black', image=arrowphoto, compound = 'right')
Goldbox=tk.Checkbutton(window,text='Booster Gold ',variable=bg, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=200,height=100,
                        activeforeground='red', activebackground='black', image=goldphoto, compound = 'right')
Marvelbox=tk.Checkbutton(window,text='Captain Marvel ',variable=m, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=210,height=100,
                        activeforeground='red', activebackground='black', image=marvelphoto, compound = 'right')
Nightbox=tk.Checkbutton(window,text='Nightwing ',variable=nw, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=170,height=100,
                        activeforeground='red', activebackground='black', image=nightphoto, compound = 'right')
Supgbox=tk.Checkbutton(window,text='Supergirl ',variable=sg, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=175,height=100, 
                        activeforeground='red', activebackground='black', image=supgphoto, compound = 'right')
Aquabox=tk.Checkbutton(window,text='Aquaman ',variable=aq, onvalue=1, offvalue=0, 
                        font=('Oswald ',12),bg= 'grey', fg='black',width=175,height=100, 
                        activeforeground='red', activebackground='black', image=aquaphoto, compound = 'right')
Supbox.place(x=10, y=300)
Wobox.place(x=220,y=300)
Batbox.place(x=10, y=415)
Flashbox.place(x=220, y=415)
Greenbox.place(x=475, y=300)
Hawkbox.place(x=430 ,y=415)
Martianbox.place(x= 640 ,y=415)
Canarybox.place(x= 905 ,y=415)
Zatannabox.place(x= 720 ,y=300)
Arrowbox.place(x= 1145 ,y=415)
Goldbox.place(x= 930 ,y=300)
Marvelbox.place(x= 1165 ,y=300)
Nightbox.place(x= 570 ,y=530)
Supgbox.place(x= 360 ,y=530)
Aquabox.place(x= 775 ,y=530)
    
def paginabatalla():
    sumapersonajes=(s.get())+(w.get())+(b.get())+(f.get()+(g.get())+(h.get())+(mm.get())+(ca.get())+(z.get())+(a.get())+(bg.get())+(m.get())+(nw.get())+
                                                  (sg.get())+(aq.get()))
    if sumapersonajes==3:
        if (usuario.get()!=''):
            window.withdraw()
            principalis()
        else:
            recordatorio=tk.Label(window,text=('DEBE ESCRIBIR SU NOMBRE, NOBLE JUGADOR'), font=('Papyrus',12,'bold'), bg='Black', fg='white')
            recordatorio.place(x=10,y=250)
            
        
    elif(s.get())+(w.get())+(b.get())+(f.get())!=3:
        recordatorio=tk.Label(window,text=('DEBE SELECCIONAR TRES PERSONAJES'), font=('Papyrus',12,'bold'))
        recordatorio.place(x=10,y=250)

        
iniciar=tk.Button(window, text='Iniciar', font=('Papyrus',12),command=paginabatalla)

iniciar.place(x=720,y=200)
window.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------
