import funcionabout
import random
import time
import csv
import tkinter as tk
from PIL import Image, ImageTk
#----------------VentanaBatallas-------------------------------------------------------------------------------------------------------------------------
def principalis():
    venjuego=tk.Toplevel()
    venjuego.geometry('1500x780')
    venjuego.resizable(False,False)
    venjuego.title('Batalla')
    canvasmenu=tk.Canvas(venjuego,bg='grey',width=300,height=420)
    nombre=tk.Label(canvasmenu,text=('Super-'+(usuario.get())), font=('Papyrus',14), bg='grey')
    sub_canvas_menu=tk.Canvas(venjuego,width=280,height=150,bg='grey')
    sub_canvas_menu.place(x=10,y=400)
    nombre.place(x=80,y=10)
    puntostitulo=tk.Label(canvasmenu, text=('Puntaje:'),bg='grey')
    puntaje=3
    puntos=tk.Label(canvasmenu, text=(puntaje),bg='grey')
    puntostitulo.place(x=100,y=40)
    puntos.place(x=100,y=60)
    canvasmenu.place(x=0, y=310)
    
    
    
    canvasvillano_1=tk.Canvas(venjuego,bg='grey',width=250,height=200)
    canvasvillano_1.place(x=1210,y=0)
    canvasvillano_2=tk.Canvas(venjuego,bg='grey',width=250,height=200)
    canvasvillano_2.place(x=1210,y=150)
    canvasvillano_3=tk.Canvas(venjuego,bg='grey',width=250,height=200)
    canvasvillano_3.place(x=1210,y=300)
    ps=tk.IntVar(value=-1)
    vil=tk.IntVar(value=-1)
    

    
    fichamalvada=tk.Label(venjuego)
    fichamalvada.place(x=1000,y=630)
    def quienes():
        id_heroe=vil.get()
        heroe=personajes[id_heroe]
        vida=heroe['vida']
        if vida<=0:
            vida=0
        ataque=heroe['ataque']
        defensa=heroe['defensa']
        
        fichamalvada.config(bd=1,relief='solid',text='Villano: '+ heroe['nombre']+
                                '\nVida: ' + str(heroe['vida']) +
                              
                                '\nAtaque: ' + str(heroe['ataque']) +
                                
                                '\nDefensa:' +  str(heroe['defensa']))
    botones_villanos={}
    villanosavencer=[]
    def supvillano():
            Supbox=tk.Radiobutton(canvasvillano_1, text="Superman", variable=vil, value=0,bg='grey',command=quienes,image=supphoto,compound='bottom')
            Supbox.place(x=0,y=0)
            Supbox.lift()
            botones_villanos[0] = Supbox
            villanosavencer.append(0)
    def batvillano():
            Batbox=tk.Radiobutton(canvasvillano_2, text="Batman", variable=vil, value=1,bg='grey',command=quienes, image=batphoto,compound='bottom')
            Batbox.place(x=0,y=0)
            Batbox.lift()
            botones_villanos[1] = Batbox
            villanosavencer.append(1)
    def wondervillano():    
            Wobox=tk.Radiobutton(canvasvillano_3, text="Wonder Woman", variable=vil, value=2,bg='grey' ,command=quienes,image=wophoto,compound='bottom')
            Wobox.place(x=0,y=0)
            Wobox.lift()
            botones_villanos[2] = Wobox
            villanosavencer.append(2)
    def flashvillano():
            Flashbox=tk.Radiobutton(canvasvillano_1, text="Flash", variable=vil, value=3, bg='grey' ,command=quienes, image=flashphoto,compound='bottom')
            Flashbox.place(x=0,y=0)
            Flashbox.lift()
            botones_villanos[3] = Flashbox
            villanosavencer.append(3)
    def greenvillano():
            Greenbox=tk.Radiobutton(canvasvillano_2, text="Green  Lantern", variable=vil, value=4, bg='grey' ,command=quienes, image=greenphoto,compound='bottom')
            Greenbox.place(x=0,y=0)
            Greenbox.lift()
            botones_villanos[4] = Greenbox
            villanosavencer.append(4)
    def hawkvillano():
            Hawkbox=tk.Radiobutton(canvasvillano_3, text="Hawkgirl", variable=vil, value=5, bg='grey',command=quienes, image=hawkphoto,compound='bottom' )
            Hawkbox.place(x=0,y=0)
            Hawkbox.lift()
            botones_villanos[5] = Hawkbox
            villanosavencer.append(5)
    def martianvillano():
            Martianbox=tk.Radiobutton(canvasvillano_1, text="Martian Manhunter", variable=vil, value=6, bg='grey' ,command=quienes, image=martianphoto,compound='bottom')
            Martianbox.place(x=0,y=0)
            Martianbox.lift()
            botones_villanos[6] = Martianbox
            villanosavencer.append(6)
    def canaryvillano():
            Canarybox=tk.Radiobutton(canvasvillano_2, text="Black Canary", variable=vil, value=7, bg='grey',command=quienes, image=canaryphoto,compound='bottom')
            Canarybox.place(x=0,y=0)
            Canarybox.lift()
            botones_villanos[7] = Canarybox
            villanosavencer.append(7)
    def zatannavillano():
            Zatannabox=tk.Radiobutton(canvasvillano_3, text="Zatanna", variable=vil, value=8, bg='grey',command=quienes,image=zatannaphoto,compound='bottom')
            Zatannabox.place(x=0,y=0)
            Zatannabox.lift()
            botones_villanos[8] = Zatannabox
            villanosavencer.append(8)
    def arrowvillano():
            Arrowbox=tk.Radiobutton(canvasvillano_1, text="Green Arrow", variable=vil, value=9, bg='grey' ,command=quienes,image=arrowphoto,compound='bottom')
            Arrowbox.place(x=0,y=0)
            Arrowbox.lift()
            botones_villanos[9] = Arrowbox
            villanosavencer.append(9)
    def goldvillano():
            Goldbox=tk.Radiobutton(canvasvillano_2, text="Booster Gold", variable=vil, value=10, bg='grey',command=quienes, image=goldphoto,compound='bottom')
            Goldbox.place(x=0,y=0)
            Goldbox.lift()
            botones_villanos[10] = Goldbox
            villanosavencer.append(10)
    def marvelvillano():            
            Marvelbox=tk.Radiobutton(canvasvillano_3, text="Captain Marvel", variable=vil, value=11, bg='grey',command=quienes, image=marvelphoto,compound='bottom')
            Marvelbox.place(x=0,y=0)
            Marvelbox.lift()
            botones_villanos[11] = Marvelbox
            villanosavencer.append(11)
    def nightvillano():
            Nightbox=tk.Radiobutton(canvasvillano_1, text="Nightwing", variable=vil, value=12, bg='grey',command=quienes, image=nightphoto,compound='bottom')
            Nightbox.place(x=0,y=0)
            Nightbox.lift()
            botones_villanos[12] = Nightbox
            villanosavencer.append(12)
    def supgvillano():
            Supgbox=tk.Radiobutton(canvasvillano_2, text="Supergirl", variable=vil, value=13, bg='grey' ,command=quienes, image=supgphoto,compound='bottom')
            Supgbox.place(x=0,y=0)
            Supgbox.lift()
            botones_villanos[13] = Supgbox
            villanosavencer.append(13)
    def aquavillano():
            Aquabox=tk.Radiobutton(canvasvillano_3, text="Aquaman", variable=vil, value=14, bg='grey',command=quienes,image=aquaphoto,compound='bottom')
            Aquabox.place(x=0,y=0)    
            Aquabox.lift()
            botones_villanos[14] = Aquabox
            villanosavencer.append(14)
            
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

    
    
   
    
    
    botones_heroes={}        
    def superheroes():        
        if (s.get())==1:
            Supper = tk.Radiobutton(sub_canvas_menu, text=  " Superman                 ",image=supphoto, variable=ps,
                                    value=0,bg='grey',compound='left',bd=1,relief='solid',command=quiensoy)
            Supper.pack(anchor='w')            
            botones_heroes[0] = Supper       
        if (b.get())==1:
            Batper = tk.Radiobutton(sub_canvas_menu, text=  " Batman                    ", variable=ps, value=1, bg='grey',
                                    compound='left',bd=1,relief='solid', image=batphoto,command=quiensoy)
            Batper.pack(anchor='w')
            botones_heroes[1] = Batper
    
        if (w.get())==1:
            Woper = tk.Radiobutton(sub_canvas_menu, text=   " Wonder Woman      ", variable=ps, value=2,bg='grey',
                                   compound='left',bd=1,relief='solid',image=wophoto,command=quiensoy)
            Woper.pack(anchor='w')
            botones_heroes[2] = Woper
             
        if (f.get())==1:
            Fper = tk.Radiobutton(sub_canvas_menu, text=    " Flash                         ", variable=ps,
                                  value=3, bg='grey',compound='left',bd=1,relief='solid', image=flashphoto,command=quiensoy)
            Fper.pack(anchor='w')
            botones_heroes[3] = Fper
    
        if (g.get())==1:
            Greenper= tk.Radiobutton(sub_canvas_menu, text= " Green Lantern          ", variable=ps, value=4,
                                     bg='grey',compound='left',bd=1,relief='solid', image=greenphoto,command=quiensoy)
            Greenper.pack(anchor='w')
            botones_heroes[4] = Greenper
             
        if (h.get())==1:
            Hawkper = tk.Radiobutton(sub_canvas_menu, text= " Hawkgirl                   ", variable=ps, value=5,
                                     bg='grey',compound='left',bd=1,relief='solid', image=hawkphoto,command=quiensoy)
            Hawkper.pack(anchor='w')
            botones_heroes[5] = Hawkper
        
        if (mm.get())==1:
            Marper = tk.Radiobutton(sub_canvas_menu, text=  " Martian Manhunter", variable=ps, value=6,
                                    bg='grey',compound='left',bd=1,relief='solid', image=martianphoto,command=quiensoy)
            Marper.pack(anchor='w')
            botones_heroes[6] = Marper
        
        if (ca.get())==1:
            Canper = tk.Radiobutton(sub_canvas_menu, text=  " Black Canary           ", image=canaryphoto, variable=ps,
                                    value=7, bg='grey',compound='left',bd=1,relief='solid',command=quiensoy)
            Canper.pack(anchor='w')
            botones_heroes[7] = Canper 

        if (z.get())==1:
            Zper = tk.Radiobutton(sub_canvas_menu, text=    " Zatanna                    ", variable=ps, value=8,
                                  bg='grey',image=zatannaphoto,compound='left',bd=1,relief='solid',command=quiensoy)
            Zper.pack(anchor='w')
            botones_heroes[8] = Zper

        if (a.get())==1:
            Arrper = tk.Radiobutton(sub_canvas_menu, text=  " Green Arrow             ", variable=ps, value=9,
                                    bg='grey',compound='left',bd=1,relief='solid',image=arrowphoto,command=quiensoy)
            Arrper.pack(anchor='w')
            botones_heroes[9] = Arrper 
        
        if (bg.get())==1:
            Gper = tk.Radiobutton(sub_canvas_menu, text=    " Booster Gold            ", variable=ps, value=10,
                                  bg='grey',compound='left',bd=1,relief='solid', image=goldphoto,command=quiensoy)
            Gper.pack(anchor='w')
            botones_heroes[10] = Gper
            
        if (m.get())==1:
            Capper = tk.Radiobutton(sub_canvas_menu, text=  " Captain Marvel         ", variable=ps,
                                    value=11, bg='grey',compound='left',bd=1,relief='solid', image=marvelphoto,command=quiensoy)
            Capper.pack(anchor='w')
            botones_heroes[11] = Capper
            
        if (nw.get())==1:
            Nightper = tk.Radiobutton(sub_canvas_menu, text=" Nightwing               ", variable=ps,
                                      value=12, bg='grey',compound='left',bd=1,relief='solid', image=nightphoto,command=quiensoy)
            Nightper.pack(anchor='w')
            botones_heroes[12] = Nightper
            
        if (sg.get())==1:
            Girlper = tk.Radiobutton(sub_canvas_menu, text= " Supergirl                 ", variable=ps,
                                     value=13, bg='grey',compound='left',bd=1,relief='solid', image=supgphoto,command=quiensoy)
            Girlper.pack(anchor='w')
            botones_heroes[13] = Girlper
        if (aq.get())==1:
            Pezper = tk.Radiobutton(sub_canvas_menu, text=  " Aquaman                    ", variable=ps, value=14, bg='grey',
                                    compound='left',bd=1,relief='solid',image=aquaphoto,command=quiensoy)
            Pezper.pack(anchor='w')
            botones_heroes[14] = Pezper
    

    canvasmapa=tk.Canvas(venjuego,bg='black',width=300,height=300)
    canvasmapa_grande=tk.Canvas(venjuego, bg='white', width=700, height=600)
    mapatitulo=tk.Label(canvasmapa, text=('Mapa'),font=('Papyrus',12),bg='black', fg='white')
    mapatitulo.place(x=120,y=10)

    def volver():
        cargar_personajes()
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        for widget in sub_canvas_menu.winfo_children():
            widget.destroy()
        superheroes()
        ganaste=tk.Canvas(venjuego,width=1500,height=780)
        gracias=tk.Label(ganaste,text=('gracias por jugar'))
        gracias.pack()
        ganaste.pack()
        ganaste.lift()
    def sub_volver():
        tapar=tk.Label(venjuego,text=('                                                                            '))
        tapar.place(x=1000,y=600)
        if puntaje==18:
            volver()
        else:
            advertencia=tk.Label(venjuego,text=('Esta ronda no ha acabado                                          '))
            advertencia.place(x=1000,y=600)
    def siguiente_4():
        cargar_personajes()
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        for widget in sub_canvas_menu.winfo_children():
            widget.destroy()
        superheroes()
        texto_ubicacion_uno=tk.Label(venjuego,text=('Atalaya                                      '),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
        texto_ubicacion_uno.place(x=100,y=200)
        boton_mapa_4=tk.Button(canvasmapa, text='Siguiente',command=sub_volver)
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
    def sub_siguiente_4():
        tapar=tk.Label(venjuego,text=('                                                                      '))
        tapar.place(x=1000,y=600)
        if puntaje==15:
            siguiente_4()
        else:
            advertencia=tk.Label(venjuego,text=('Esta ronda no ha acabado                                 '))
            advertencia.place(x=1000,y=600)
    def siguiente_3():
        cargar_personajes()
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        for widget in sub_canvas_menu.winfo_children():
            widget.destroy()
        superheroes()
        texto_ubicacion_uno=tk.Label(venjuego,text=('Sala de Entrenamiento'),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
        texto_ubicacion_uno.place(x=100,y=200)
        boton_mapa_4=tk.Button(canvasmapa, text='Siguiente',command=sub_siguiente_4)
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
    def sub_siguiente_3():
        tapar=tk.Label(venjuego,text=('                                                                      '))
        tapar.place(x=1000,y=600)
        if puntaje==12:
            siguiente_3()
        else:
            advertencia=tk.Label(venjuego,text=('Esta ronda no ha acabado                                     '))
            advertencia.place(x=1000,y=600)
    def siguiente_2():
        cargar_personajes()
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        for widget in sub_canvas_menu.winfo_children():
            widget.destroy()
        superheroes()
        texto_ubicacion_uno=tk.Label(venjuego,text=('Sala de Reuniones'),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
        texto_ubicacion_uno.place(x=100,y=200)
        boton_mapa_3=tk.Button(canvasmapa, text='Siguiente',command=sub_siguiente_3)
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
    def sub_siguiente_2():
        tapar=tk.Label(venjuego,text=('                                                                                 '))
        tapar.place(x=1000,y=600)
        if puntaje==9:
            siguiente_2()
        else:
            advertencia=tk.Label(venjuego,text=('Esta ronda no ha acabado                             '))
            advertencia.place(x=1000,y=600)
        
    def siguiente_1():
        cargar_personajes()
        for widget in canvasvillano_1.winfo_children():
            widget.destroy()

        for widget in canvasvillano_2.winfo_children():
            widget.destroy()

        for widget in canvasvillano_3.winfo_children():
            widget.destroy()
        for widget in sub_canvas_menu.winfo_children():
            widget.destroy()
        superheroes()
       
        
        texto_ubicacion_uno=tk.Label(venjuego,text=('Salón de la Justicia'),bg='black',fg='white',font=('Papyrus',12), compound='bottom')
        texto_ubicacion_uno.place(x=100,y=200)
        boton_mapa_2=tk.Button(canvasmapa, text='Siguiente',command=sub_siguiente_2)
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
    def sub_siguiente_1():
        tapar=tk.Label(venjuego,text=('                                                                               '))
        tapar.place(x=1000,y=600)
        if puntaje==6:
            siguiente_1()
        else:
            advertencia=tk.Label(venjuego,text=('Esta ronda no ha acabado                            '))
            advertencia.place(x=1000,y=600)
        
        
        
    boton_mapa=tk.Button(canvasmapa, text='Siguiente',command=sub_siguiente_1)
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
    personajes={}
    
    def cargar_personajes():
        archivo = open("Personajes.txt", "r", encoding="utf-8")
        lector = csv.DictReader(archivo)

        for fila in lector:
            id_personaje = int(fila["id"])

            personajes[id_personaje] = {
                "nombre": fila["nombre"],
                "ataque": int(fila["ataque"]),
                "vida": int(fila["vida"]),
                "defensa": int(fila["defensa"])
            }

        archivo.close()
    fichapersonaje=tk.Label(venjuego)
    fichapersonaje.place(x=450,y=630)


    
    def quiensoy():
        id_heroe=ps.get()
        heroe=personajes[id_heroe]
        vida=heroe['vida']
        if vida<=0:
            vida=0
        ataque=heroe['ataque']
        defensa=heroe['defensa']
        
        fichapersonaje.config(bd=1,relief='solid',text='Personaje: '+ heroe['nombre']+
                                '\nVida: ' + str(heroe['vida']) +
                                '\nAtaque: ' + str(heroe['ataque']) +
                                '\nDefensa:' +  str(heroe['defensa']))

    
        

        
    cargar_personajes()
    
    def defender():
            quienes()
            quiensoy()
            tapar=tk.Label(venjuego,text=('                                                                    '))
            tapar.place(x=1000,y=600)
        
        
            id_heroe=vil.get()
            id_villano=ps.get()
            heroe = personajes[id_heroe]
            villano=personajes[id_villano]
            if heroe['vida']<=0 or villano['vida']<0:
                advertencia=tk.Label(venjuego,text=('Tu personaje ha muerto, escoje otro'))
                advertencia.place(x=1000,y=600)
                
                    
            else:
            
                time.sleep(3)
                fight.place(x=780, y=600)
                daño = heroe['ataque'] - villano['defensa']
                villano['vida'] = villano['vida'] - daño
        
                quienes()
                quiensoy()
                if villano['vida']<=0:
                    
                    botones_heroes[id_villano].destroy()
                

                    
    def atacar():
        tapar=tk.Label(venjuego,text=('                                                                    '))
        tapar.place(x=1000,y=600)
        nonlocal puntaje
        id_heroe = ps.get()
        id_villano = vil.get()
        heroe = personajes[id_heroe]
        villano = personajes[id_villano]
        if ps.get()==-1 or vil.get()==-1:
            advertencia=tk.Label(venjuego,text=('No hay heroe'))
            advertencia.place(x=1000,y=600)
        else:
            if heroe['vida']<=0 or villano['vida']<=0:
                    advertencia=tk.Label(venjuego,text=('Tu personaje ha muerto, escoje otro'))
                    advertencia.place(x=1000,y=600)
                    malomalisimo=random.choice(villanosavencer)
                    vil.set(malomalisimo)
            
            else:
                    time.sleep(3)
                    resist.place(x=780,y=600)
                    fight.place(x=190678)
                    daño = heroe['ataque'] - villano['defensa']
                    villano['vida'] = villano['vida'] - daño
                    
                    
                    quienes()
                    quiensoy()
                    if villano['vida']<=0:
                        
                        botones_villanos[id_villano].destroy()
                        puntaje+=1
                        puntos=tk.Label(canvasmenu, text=(puntaje),bg='grey')
                        puntostitulo.place(x=100,y=40)
                        puntos.place(x=100,y=60)
                        
           
                    
            
        
    resist=tk.Button(venjuego, text=('Defender'), command=defender)
    fight=tk.Button(venjuego, text=('   Atacar   '), command=atacar)
    fight.place(x=780, y=600)
  
    superheroes()
     
    venjuego.mainloop()
#--------------------------------------------------------------------------------
#VentanaPrincipal
#----------------------------------------------------------------------------------------------
window=tk.Tk()
window.geometry('1500x700')
window.title('Proyecto Intro')
window.resizable(False,False)

about = tk.Button(window,text=('About'),font=('Papyrus',12),command=funcionabout.botonabout)
about.pack() #boton about

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
opcionuno=Image.open('opcionuno.png')#imagenes
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
batphoto=ImageTk.PhotoImage(batphoto_resize)#puro resize

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
mm=tk.IntVar() #int vars
ca=tk.IntVar()
z=tk.IntVar()
a=tk.IntVar()
bg=tk.IntVar()
m=tk.IntVar()
nw=tk.IntVar()
sg=tk.IntVar()
aq=tk.IntVar()

Supbox=tk.Checkbutton(window,text='Superman ',variable=s, onvalue=1, offvalue=0, #personajes
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
            recordatorio=tk.Label(window,text=('DEBE ESCRIBIR SU NOMBRE                   '), font=('Papyrus',12,'bold'), fg='black')
            recordatorio.place(x=10,y=250)
            
        
    elif(s.get())+(w.get())+(b.get())+(f.get())!=3:
        recordatorio=tk.Label(window,text=('DEBE SELECCIONAR TRES PERSONAJES'), font=('Papyrus',12,'bold'))
        recordatorio.place(x=10,y=250)

        
iniciar=tk.Button(window, text='Iniciar', font=('Papyrus',12),command=paginabatalla)

iniciar.place(x=720,y=200)
window.mainloop()

#----------------------------------------------------------------------------------------------------------------------------------------------------------
