import tkinter as tk

def crear_opciones(ventana):
    u = tk.IntVar()
    u.set(-1)   # ninguna seleccionada al inicio

    def seleccionar_ubicacion():
        if (s.get() )== 0:
            print("UB1")
            rb1 = tk.Radiobutton(canvasmenu, text="Salon Justicia", variable=u, value=0,
                         command=seleccionar_ubicacion)
            rb1.pack(anchor='w')

        elif u.get() == 1:
            print("UB2")
        elif u.get() == 2:
            print("UB3")
        elif u.get() == 3:
            print("UB4")
        elif u.get() == 4:
            print("UB5")

    rb1 = tk.Radiobutton(ventana, text="Salon Justicia", variable=u, value=0,
                         command=seleccionar_ubicacion)
    rb1.pack(anchor='w')

    rb2 = tk.Radiobutton(ventana, text="Patio Principal", variable=u, value=1,
                         command=seleccionar_ubicacion)
    rb2.pack(anchor='w')

    rb3 = tk.Radiobutton(ventana, text="Sala de Entrenamiento", variable=u, value=2,
                         command=seleccionar_ubicacion)
    rb3.pack(anchor='w')

    rb4 = tk.Radiobutton(ventana, text="Sala de Reuniones", variable=u, value=3,
                         command=seleccionar_ubicacion)
    rb4.pack(anchor='w')

    rb5 = tk.Radiobutton(ventana, text="Atalaya", variable=u, value=4,
                         command=seleccionar_ubicacion)
    rb5.pack(anchor='w')

def principal():
    ventana = tk.Tk()
    ventana.geometry("300x250")

    crear_opciones(ventana)

    ventana.mainloop()

principal()






