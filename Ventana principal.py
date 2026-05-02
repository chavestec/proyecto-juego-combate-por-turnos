import funcionabout
import random
import time
import tkinter as tk
from PIL import Image, ImageTk
#----------------VentanaBatallas-------------------------------------------------------------------------------------------------------------------------
def principalis():
    venjuego=tk.Toplevel()
    venjuego.geometry('1500x675')
    venjuego.resizable(False,False)
    venjuego.title('Batalla')
    canvasmenu=tk.Canvas(venjuego,bg='grey',width=300,height=300)
    nombre=tk.Label(canvasmenu,text=('Super-'+(usuario.get())), font=('Papyrus',14), bg='grey')
    sub_canvas_menu=tk.Canvas(venjuego,width=280,height=150,bg='grey')
    sub_canvas_menu.place(x=10,y=400)
    nombre.place(x=80,y=10)
    puntostitulo=tk.Label(canvasmenu, text=('Puntaje:'),bg='grey')
    sumapersonajes=(s.get())+(w.get())+(b.get())+(f.get()+(g.get())+(h.get())+(mm.get())+(ca.get())+(z.get())+(a.get())+(bg.get())+(m.get())+(nw.get())+
                                                  (sg.get())+(aq.get()))
    puntos=tk.Label(canvasmenu, text=(sumapersonajes),bg='grey')
    puntostitulo.place(x=200,y=10)
    puntos.place(x=200,y=30)
    canvasmenu.place(x=0, y=310)
    
    
    
    canvasvillano_1=tk.Canvas(venjuego,bg='grey',width=250,height=200)
    canvasvillano_1.place(x=1210,y=0)
    canvasvillano_2=tk.Canvas(venjuego,bg='grey',width=250,height=200)
    canvasvillano_2.place(x=1210,y=150)
    canvasvillano_3=tk.Canvas(venjuego,bg='grey',width=250,height=200)
    canvasvillano_3.place(x=1210,y=300)
    ps=tk.IntVar()
    vil=tk.IntVar()
    def villanos():
       
        
            if vil.get()==0:
                print ('Superman')
            elif vil.get()==1:
                print ('Batman')
            elif vil.get()==2:
                print('Wonder Woman')
            elif vil.get()==3:
                print('Flash')
            elif vil.get()==4:
                print('Green Lantern')
            elif vil.get()==5:
                print('Hawkgril')
            elif vil.get()==6:
                print('Martian')
            elif vil.get()==7:
                print('Canary')
            elif vil.get()==8:
                print('Zatanna')
            elif vil.get()==9:
                print('Arrow')
            elif vil.get()==10:
                print('Booster')
            elif vil.get()==11:
                print('Marvel')
            elif vil.get()==12:
                print('Nightwing')
            elif vil.get()==13:
                print('Supergirl')
            elif vil.get()==14:
                print('Aquaman')

    def supvillano():
            Supbox=tk.Radiobutton(canvasvillano_1, text="Superman",image=supphoto, variable=vil, value=0,bg='grey',command=villanos)
            
            Supbox.place(x=0,y=0)
            Supbox.lift()

    def batvillano():
            Batbox=tk.Radiobutton(canvasvillano_2, text="Wonder Woman", variable=vil, value=2,bg='grey',command=villanos)
            Batbox.place(x=0,y=0)
            Batbox.lift()
 
    def wondervillano():    
            Wobox=tk.Radiobutton(canvasvillano_3, text="Wonder Woman", variable=vil, value=2,bg='grey',command=villanos)
            Wobox.place(x=0,y=0)
            Wobox.lift()
    def flashvillano():
             
            Flashbox=tk.Radiobutton(canvasvillano_1, text="Flash", variable=vil, value=3, bg='grey',command=villanos)
            Flashbox.place(x=0,y=0)
            Flashbox.lift()
    def greenvillano():
            Greenbox=tk.Radiobutton(canvasvillano_2, text="Green  Lantern", variable=vil, value=4, bg='grey',command=villanos)
            Greenbox.place(x=0,y=0)
            Greenbox.lift()
    def hawkvillano():
             
            Hawkbox=tk.Radiobutton(canvasvillano_3, text="Hawkgirl", variable=vil, value=5, bg='grey',command=villanos)
            Hawkbox.place(x=0,y=0)
            Hawkbox.lift()
    def martianvillano():
             
            Martianbox=tk.Radiobutton(canvasvillano_1, text="Martian Manhunter", variable=vil, value=6, bg='grey',command=villanos)
            Martianbox.place(x=0,y=0)
            Martianbox.lift()
    def canaryvillano():
             
            Canarybox=tk.Radiobutton(canvasvillano_2, text="Black Canary", variable=vil, value=7, bg='grey',command=villanos)
            Canarybox.place(x=0,y=0)
            Canarybox.lift()
    def zatannavillano():
             
            Zatannabox=tk.Radiobutton(canvasvillano_3, text="Zatanna", variable=vil, value=8, bg='grey',command=villanos)
            Zatannabox.place(x=0,y=0)
            Zatannabox.lift()
    def arrowvillano():
             
            Arrowbox=tk.Radiobutton(canvasvillano_1, text="Green Arrow", variable=vil, value=9, bg='grey',command=villanos)
            Arrowbox.place(x=0,y=0)
            Arrowbox.lift()
    def goldvillano():
             
            Goldbox=tk.Radiobutton(canvasvillano_2, text="Booster Gold", variable=vil, value=10, bg='grey',command=villanos)
            Goldbox.place(x=0,y=0)
            Goldbox.lift()
    def marvelvillano():
             
            Marvelbox=tk.Radiobutton(canvasvillano_3, text="Captain Marvel", variable=vil, value=11, bg='grey',command=villanos)
            Marvelbox.place(x=0,y=0)
            Marvelbox.lift()
    def nightvillano():
             
            Nightbox=tk.Radiobutton(canvasvillano_1, text="Captain Marvel", variable=vil, value=12, bg='grey',command=villanos)
            Nightbox.place(x=0,y=0)
            Nightbox.lift()
    def supgvillano():
             
            Supgbox=tk.Radiobutton(canvasvillano_2, text="Supergirl", variable=vil, value=13, bg='grey',command=villanos)
            Supgbox.place(x=0,y=0)
            Supgbox.lift()

    def aquavillano():
             
            Aquabox=tk.Radiobutton(canvasvillano_3, text="Aquaman", variable=vil, value=14, bg='grey',command=villanos)
            Aquabox.place(x=0,y=0)    
            Aquabox.lift()
            
    posiblesvillanos_1=[]
    posiblesvillanos_2=[]
    posiblesvillanos_3=[]

        
        
    if(s.get())==0:
            posiblesvillanos_1.append(supvillano)
            
    if(b.get())==0:
             posiblesvillanos_2.append(batvillano)
            
    if (w.get())==0:
            posiblesvillanos_3.append(wondervillano)    
                
    if (f.get())==0:
            posiblesvillanos_1.append(flashvillano)
            
    if(g.get())==0:
            posiblesvillanos_2.append(greenvillano)

    if (h.get())==0:
            posiblesvillanos_3.append(hawkvillano)

    if (mm.get())==0:
            posiblesvillanos_1.append(martianvillano)

    if (ca.get())==0:
            posiblesvillanos_2.append(canaryvillano)

    if (z.get())==0:
            posiblesvillanos_3.append(zatannavillano)

    if (a.get())==0:
            posiblesvillanos_1.append(arrowvillano)

    if (bg.get())==0:
            posiblesvillanos_2.append(goldvillano)

    if (m.get())==0:
            posiblesvillanos_3.append(marvelvillano)

    if (nw.get())==0:
            posiblesvillanos_1.append(nightvillano)

    if (sg.get())==0:
            posiblesvillanos_2.append(supgvillano)

    if (aq.get())==0:
            posiblesvillanos_3.append(aquavillano)

    villanouno =random.choice(posiblesvillanos_1)
    villanouno()

    villanodos =random.choice(posiblesvillanos_2)
    villanodos()

    villanotres =random.choice(posiblesvillanos_3)
    villanotres()
                
    
    def seleccionado():
            if ps.get()==0:
                print ('Superman')
            elif ps.get()==1:
                print ('Batman')
            elif ps.get()==2:
                print('Wonder Woman')
            elif ps.get()==3:
                print('Flash')
            elif ps.get()==4:
                print('Green Lantern')
            elif ps.get()==5:
                print('Hawkgril')
            elif ps.get()==6:
                print('Martian')
            elif ps.get()==7:
                print('Canary')
            elif ps.get()==8:
                print('Zatanna')
            elif ps.get()==9:
                print('Arrow')
            elif ps.get()==10:
                print('Booster')
            elif ps.get()==11:
                print('Marvel')
            elif ps.get()==12:
                print('Nightwing')
            elif ps.get()==13:
                print('Supergirl')
            elif ps.get()==14:
                print('Aquaman')
            
            
    if (s.get())==1:
            rb1 = tk.Radiobutton(sub_canvas_menu, text="Superman",image=supphoto, variable=ps, value=0,bg='grey',command=seleccionado)
            rb1.pack(anchor='w')            
                    
    if (b.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Batman", variable=ps, value=1, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')

    
    if (w.get())==1:
            rb1 = tk.Radiobutton(sub_canvas_menu, text="Wonder Woman", variable=ps, value=2,bg='grey',command=seleccionado)
            rb1.pack(anchor='w')
             
    
    if (f.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Flash", variable=ps, value=3, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
             
    
    if (g.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Green  Lantern", variable=ps, value=4, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')

             
    if (h.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Hawkgirl", variable=ps, value=5, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
             
        
    if (mm.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Martian Manhunter", variable=ps, value=6, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
             
        
    if (ca.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Black Canary", variable=ps, value=7, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
             

    if (z.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Zatanna", variable=ps, value=8, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
             

    if (a.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Green Arrow", variable=ps, value=9, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
             
        
    if (bg.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Booster Gold", variable=ps, value=10, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
             
            
    if (m.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Captain Marvel", variable=ps, value=11, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
        
            
    if (nw.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Captain Marvel", variable=ps, value=12, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
        
            
            
    if (sg.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Supergirl", variable=ps, value=13, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
        
    if (aq.get())==1:
            rb2 = tk.Radiobutton(sub_canvas_menu, text="Aquaman", variable=ps, value=14, bg='grey',command=seleccionado)
            rb2.pack(anchor='w')
        
    

    canvasmapa=tk.Canvas(venjuego,bg='black',width=300,height=300)
    canvasmapa_grande=tk.Canvas(venjuego, bg='white', width=700, height=600)
    mapatitulo=tk.Label(canvasmapa, text=('Mapa'),font=('Papyrus',12),bg='black', fg='white')
    mapatitulo.place(x=120,y=10)

    def volver():
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        boton_mapa.lift()
        texto_ubicacion_uno.lift()
        fonduno_original=Image.open('fondo.png')
        fonduno_resize=fonduno_original.resize((130,130))
        fonduno=ImageTk.PhotoImage(fonduno_resize)
        canvasmapa.create_image(80,50,image=fonduno,anchor=tk.NW)
        canvasmapa.image=fonduno
        
        fonduno_copy_original=Image.open('fondo_copy.png')
        fonduno_copy__resize=fonduno_copy_original.resize((700,600))
        fonduno_copy_=ImageTk.PhotoImage(fonduno_copy__resize)
        canvasmapa_grande.create_image(0,0,image=fonduno_copy_,anchor=tk.NW)
        canvasmapa_grande.image=fonduno_copy_
        
        villanouno =random.choice(posiblesvillanos_1)
        villanouno()

        villanodos =random.choice(posiblesvillanos_2)
        villanodos()  

        villanotres =random.choice(posiblesvillanos_3)
        villanotres()
    def siguiente_4():
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        texto_ubicacion_uno=tk.Label(venjuego,text=('Atalaya                                      '),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
        texto_ubicacion_uno.place(x=100,y=200)
        boton_mapa_4=tk.Button(canvasmapa, text='Siguiente',command=volver)
        boton_mapa_4.place(x=115,y=230)
        fonata_original=Image.open('fonata.png')
        fonata_resize=fonata_original.resize((130,130))
        fonata=ImageTk.PhotoImage(fonata_resize)
        canvasmapa.create_image(80,50,image=fonata,anchor=tk.NW)
        canvasmapa.image=fonata

        fonata_copy_original=Image.open('fonata_copy.png')
        fonata_copy__resize=fonata_copy_original.resize((700,600))
        fonata_copy_=ImageTk.PhotoImage(fonata_copy__resize)
        canvasmapa_grande.create_image(0,0,image=fonata_copy_,anchor=tk.NW)
        canvasmapa_grande.image=fonata_copy_

        villanouno =random.choice(posiblesvillanos_1)
        villanouno()

        villanodos =random.choice(posiblesvillanos_2)
        villanodos()  

        villanotres =random.choice(posiblesvillanos_3)
        villanotres()
    def siguiente_3():
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        texto_ubicacion_uno=tk.Label(venjuego,text=('Sala de Entrenamiento'),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
        texto_ubicacion_uno.place(x=100,y=200)
        boton_mapa_4=tk.Button(canvasmapa, text='Siguiente',command=siguiente_4)
        boton_mapa_4.place(x=115,y=230)
        fondos_original=Image.open('fondos.png')
        fondos_resize=fondos_original.resize((130,130))
        fondos=ImageTk.PhotoImage(fondos_resize)
        canvasmapa.create_image(80,50,image=fondos,anchor=tk.NW)
        canvasmapa.image=fondos

        fondos_copy_original=Image.open('fondos_copy.png')
        fondos_copy__resize=fondos_copy_original.resize((700,600))
        fondos_copy_=ImageTk.PhotoImage(fondos_copy__resize)
        canvasmapa_grande.create_image(0,0,image=fondos_copy_,anchor=tk.NW)
        canvasmapa_grande.image=fondos_copy_
        
        villanouno =random.choice(posiblesvillanos_1)
        villanouno()

        villanodos =random.choice(posiblesvillanos_2)
        villanodos()  

        villanotres =random.choice(posiblesvillanos_3)
        villanotres()
    def siguiente_2():
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        texto_ubicacion_uno=tk.Label(venjuego,text=('Sala de Reuniones'),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
        texto_ubicacion_uno.place(x=100,y=200)
        boton_mapa_3=tk.Button(canvasmapa, text='Siguiente',command=siguiente_3)
        boton_mapa_3.place(x=115,y=230)
        fontres_original=Image.open('fontres.png')
        fontres_resize=fontres_original.resize((130,130))
        fontres=ImageTk.PhotoImage(fontres_resize)
        canvasmapa.create_image(80,50,image=fontres,anchor=tk.NW)
        canvasmapa.image=fontres

        fontres_copy_original=Image.open('fontres_copy.png')
        fontres_copy__resize=fontres_copy_original.resize((700,600))
        fontres_copy_=ImageTk.PhotoImage(fontres_copy__resize)
        canvasmapa_grande.create_image(0,0,image=fontres_copy_,anchor=tk.NW)
        canvasmapa_grande.image=fontres_copy_

        villanouno =random.choice(posiblesvillanos_1)
        villanouno()

        villanodos =random.choice(posiblesvillanos_2)
        villanodos()  

        villanotres =random.choice(posiblesvillanos_3)
        villanotres()
    def siguiente_1():
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        texto_ubicacion_uno=tk.Label(venjuego,text=('Salón de la Justicia'),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
        texto_ubicacion_uno.place(x=100,y=200)
        boton_mapa_2=tk.Button(canvasmapa, text='Siguiente',command=siguiente_2)
        boton_mapa_2.place(x=115,y=230)
        foncu_original=Image.open('foncu.png')
        foncu_resize=foncu_original.resize((130,130))
        foncu=ImageTk.PhotoImage(foncu_resize)
        canvasmapa.create_image(80,50,image=foncu,anchor=tk.NW)
        canvasmapa.image=foncu

        foncu_copy_original=Image.open('foncu_copy.png')
        foncu_copy__resize=foncu_copy_original.resize((700,600))
        foncu_copy_=ImageTk.PhotoImage(foncu_copy__resize)
        canvasmapa_grande.create_image(0,0,image=foncu_copy_,anchor=tk.NW)
        canvasmapa_grande.image=foncu_copy_
        villanouno =random.choice(posiblesvillanos_1)
        villanouno()

        villanodos =random.choice(posiblesvillanos_2)
        villanodos()  

        villanotres =random.choice(posiblesvillanos_3)
        villanotres()
        
    boton_mapa=tk.Button(canvasmapa, text='Siguiente',command=siguiente_1)
    boton_mapa.place(x=115,y=230)
    texto_ubicacion_uno=tk.Label(venjuego,text=('Patio Principal'),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
    texto_ubicacion_uno.place(x=100,y=200)
    canvasmapa.place(x=0,y=0)
    canvasmapa_grande.place(x=400)
    fonduno_original=Image.open('fondo.png')
    fonduno_resize=fonduno_original.resize((130,130))
    fonduno=ImageTk.PhotoImage(fonduno_resize)
    canvasmapa.create_image(80,50,image=fonduno,anchor=tk.NW)
    canvasmapa.image=fonduno

    fonduno_copy_original=Image.open('fondo_copy.png')
    fonduno_copy__resize=fonduno_copy_original.resize((700,600))
    fonduno_copy_=ImageTk.PhotoImage(fonduno_copy__resize)
    canvasmapa_grande.create_image(0,0,image=fonduno_copy_,anchor=tk.NW)
    canvasmapa_grande.image=fonduno_copy_

    if (av.get())==0:
        opcionuno=Image.open('opcionuno_dos.png')
        avataruno=opcionuno.resize((50,50))
        uno=ImageTk.PhotoImage(avataruno)
        canvasmenu.create_image(10,10,image=uno,anchor=tk.NW)
        canvasmenu.image=uno
    elif (av.get())==1:
        opcionuno=Image.open('opcion2.png')
        avataruno=opcionuno.resize((50,50))
        uno=ImageTk.PhotoImage(avataruno)
        canvasmenu.create_image(10,10,image=uno,anchor=tk.NW)
        canvasmenu.image=uno
    elif (av.get())==2:
        opcionuno=Image.open('proteger.png')
        avataruno=opcionuno.resize((50,50))
        uno=ImageTk.PhotoImage(avataruno)
        canvasmenu.create_image(10,10,image=uno,anchor=tk.NW)
        canvasmenu.image=uno

    x=ps.get()
    y=vil.get()
    
    def defender():
        time.sleep(3)
        resist.place(y=90000)
        fight.place(x=600, y=600)
    def atacar(x,y):
        fight.place(x=100000000000000000000000)
        time.sleep(3)
        resist.place(x=600, y=600)
        resist.lift()

        
      
        
    resist=tk.Button(venjuego, text=('Defender'), command=defender)
    fight=tk.Button(venjuego, text=('  Atacar  '), command=atacar)
    fight.place(x=600, y=600)
  
    seleccionado()
    villanos() 
    venjuego.mainloop()
#--------------------------------------------------------------------------------
#VentanaPrincipal
#----------------------------------------------------------------------------------------------
window=tk.Tk()
window.geometry('1500x700')
window.title('Proyecto Intro')
window.resizable(False,False)

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
usuario.config(font=('Papyrus',14))
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
            recordatorio=tk.Label(window,text=('DEBE ESCRIBIR SU NOMBRE'), font=('Papyrus',12,'bold'), fg='black')
            recordatorio.place(x=10,y=250)
            
        
    elif(s.get())+(w.get())+(b.get())+(f.get())!=3:
        recordatorio=tk.Label(window,text=('DEBE SELECCIONAR TRES PERSONAJES'), font=('Papyrus',12,'bold'))
        recordatorio.place(x=10,y=250)

        
iniciar=tk.Button(window, text='Iniciar', font=('Papyrus',12),command=paginabatalla)

iniciar.place(x=720,y=200)
window.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------
