import tkinter as tk
def principalis():
    venjuego=tk.Tk()
    venjuego.geometry('1500x700')
    venjuego.resizable(False,False)
    venjuego.title('Batalla')
    info=tk.Label(venjuego,text=('Juego'), font= ('Arial',12))
    info.pack()
    def supguardado():
        if ventanaprincipal.s==1:
            supcarta=tk.Label(venjuego, text=('Aqui'),font=('Arial',12))
            supcarta.pack()
        elif(s.get())==0:
            nosupcarta=tk.Label(venjuego, text=('Aqui no'),font=('Arial',12))
            nosupcarta.pack()
        else:
            nosupcartaa=tk.Label(venjuego, text=('Aqui menos'),font=('Arial',12))
            nosupcartaa.pack()
        
         
    venjuego.mainloop()
