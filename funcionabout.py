import tkinter as tk
n=
El presente documento describe la creación, el funcionamiento y todas las generalidades de un proyecto que consistía en realizar un juego de combate por turnos en Python. Este proyecto se basa principalmente en la biblioteca de Tkinter en Python. Esta permite diseñar interfaces gráficas sencillas, lo que fue de gran ayuda en la realización del proyecto. La idea del juego es la siguiente: el jugador ingresa su nombre y selecciona tres personajes de una lista de quince, para luego enfrentarse a todos los otros a lo largo de cinco niveles. Cada personaje tiene atributos de vida, ataque y defensa, lo que permite que los enfrentamientos sean interesantes y diferentes entre sí. Los turnos se dividen en uno de ataque y uno de defensa, al estilo Pokemon. Al final, el objetivo del juego es llegar hasta el último nivel, tras haber derrotado a quince enemigos. Estos enemigos se pueden repetir y verdaderamente no hay que necesariamente vencerlos a todos para ganar.
Dentro del proyecto se usan los personajes de la Liga de la Justicia, de DC Comics como personajes jugables y enemigos. Cada personaje tiene atributos de acorde a sus niveles de poder.
La realización de este proyecto requería aplicar los conocimientos aprendidos en la clase de Introducción a la Programación, como el uso de listas, funciones, recursividad y variables. Así mismo, también era necesario aprender de temas como el uso de Tkinter y todas sus funcionalidades, diccionarios, lectura de archivos CSV y entre otros.


Conclusiones
Al final, se consiguió realizar el juego de manera funcional con una interfaz gráfica en Python, realizada mediante Tkinter. En esta se pueden escoger los personajes y ponerlos a luchar hasta encontrar un ganador. La interfaz gráfica de Tkinter traía problemas, aunque al final cumplió su cometido y sí es factible usarla para la realización de juegos sencillos.
El archivo CSV demostró ser útil para importar datos y mejorar la manera que la información está distribuida ya que al ser una gran cantidad de información, era mejor leerla desde otro archivo que tenerla ahí guardada dentro del código.
Se entiende que la cantidad de funciones utilizadas no es la óptima recomendable, por lo que se trabajará en ello para proyectos futuros.
El proyecto permitió un mayor entendimiento de los temas estudiados en clase, por lo que se considera de gran valor y utilidad para avanzar como programador.






Recomendaciones
	En base a las experiencias vividas durante la realización del proyecto, se proponen las siguientes recomendaciones:
Mejorar en el uso de Tkinter para una experiencia más fluida si este se necesita para algún proyecto futuro.
Incorporar el uso de clases en vez de la lectura de un archivo CSV podría facilitar la realización de proyectos de este tipo, y ayudaría a entender mejor la programación orientada a objetos. Además, esto reduciría la complejidad del código.
Agregar animaciones o música para tener una experiencia más interactiva o disfrutable para los usuarios que prueben el juego. Aunque para esto se ocuparía Pygame o sería casi imposible.
Se podría distribuir el código en varios archivos para que sea más fácil comprenderlo o cambiarlo más adelante.
Se debería mejorar el manejo de excepciones en caso de error para que el juego no se rompa de manera sencilla.
















Análisis de resultados
	La página principal funciona, pues se pueden escoger tres personajes, digitar su nombre y escoger un avatar que lo acompañará el resto de la partida.	El programa no permite al usuario avanzar si este escogió un número diferente a tres personajes.
	Al momento de escribir esto, el programa funciona de manera parcial, y tiene problemas en el uso de la aleatoriedad para escoger los villanos a los que debe enfrentarse el usuario con sus personajes.
	Aparte de esto, el reconocimiento de los atributos de los personajes se realiza de manera perfecta, y los cálculos de daño en las batallas entre personajes también funcionan de gran manera.
	La lectura de datos de un archivo CSV y la posterior conversión de estos datos a un diccionario funciona. Además, estos datos pueden actualizarse después de cada batalla, por lo que los personajes van perdiendo vida a lo largo de las partidas.
	Uno de los aspectos más difíciles fue el manejo de los widgets de Tkinter, especialmente al tratar de eliminarlos, pero finalmente se logró un resultado satisfactorio respectos a esto y ya se pueden borrar cuando es necesario para el funcionamiento del programa.
	Finalmente se logró encontrarle un final al juego, y el desarrollo de dicha pantalla final también está presente en el proyecto.

Explicación de bibliotecas utilizadas y código generado por IA 
Bibliotecas:
Tkinter: realización de toda la interfaz gráfica. Permite la creación de widgets como Radio Buttons, Labels, Canvas, y ventanas. Es la parte con la que interactúa el usuario.
CSV: funciona para leer o editar archivos que contienen datos separados por comas. En este caso solo se usó para leer.
Random: permite utilizar varias funciones relacionadas a la aleatoriedad. Se utilizó para el funcionamiento del rival del usuario y escoger los personajes rivales.
Time: esta funciona para invocar datos de tiempo. Se usó para pausar algunas funciones por un tiempo para que el juego fuera más pausado.
Pillow: esta fue usada para manipular imágenes y utilizarlas de cierto tamaño específico en el código.

Código generado por IA
Se utilizó Chat GPT para la evacuación de dudas y para ciertas secciones del código. La IA realizó la función que elimina widgets de un canvas ya que se consideró imposible hacerlo de otra manera. Además, la IA proporcionó ideas de como hacer la selección aleatoria de villanos en cada nivel, aunque esto después se realizó de otra manera





Los personajes jugables se escogen en la ventana principal, y luego todo lo demás se maneja en la ventana de batallas, dentro de una función llamada principalis()

Diagrama de Módulos del Sistema
Ventana_principal_copy.py
•        window: Ventana principal de Tkinter con selección de nombre, avatar y héroes.
•        prograbotonuser(): Muestra el nombre del jugador.
•        avatar_seleccionado(): Para escoger el avatar.
•        paginabatalla(): Para escoger los tres personajes jugables
•        principalis(): Función principal de la ventana de batalla.
Submódulos dentro de principalis():
•        cargar_personajes(): Mete los personajes del CSV a un diccionario.
•        superheroes(): Crea los Radiobuttons de los personajes jugables.
•        supvillano(), batvillano()... : Crean Radiobuttons de villanos.
•        quiensoy(): Actualiza la ficha del héroe que se está usando.
•        quienes(): Actualiza la ficha del villano que se está enfrentando al heroe.
•        atacar(): Para atacar al villano.
•        defender(): El villano ataca al personaje jugable.
•        Desde siguiente_1() hasta siguiente_4(): Avanzan a la siguiente ubicación del mapa.
•        sub_siguiente_1() a sub_volver(): Validan el puntaje antes de avanzar de ronda.
Módulos externos:
•        funcionabout.py: Crea una ventana con el about del proyecto.
•        Personajes.txt: Aquí están guardados los atributos de los personajes.
•        Archivos PNG: Imágenes de personajes  y fondos para los niveles.
















Literatura y Fuentes
Commit That Line! (2021, 23 mayo). ¿Cómo usar CLASES en PYTHON? [Vídeo]. YouTube. https://www.youtube.com/watch?v=9x7RK6mb1uA 

Python tkinter tutorial for beginners 🐍. (s. f.). YouTube. https://www.youtube.com/playlist?list=PLZPZq0r_RZOOeQBaP5SeMjl2nwDcJaV0T 
Código Espinoza - Automatiza tu Vida. (2023, 29 mayo). Curso de Tkinter Python: ¿Cómo Cargar y Manipular Imágenes en Tkinter con Python? con PIL! | E12 [Vídeo]. YouTube. https://www.youtube.com/watch?v=Rxq1C1Usq3U 

Corey Schafer. (2017, 9 agosto). Python Tutorial: CSV Module - How to Read, Parse, and Write CSV Files [Vídeo]. YouTube. https://www.youtube.com/watch?v=q5uM4VKywbA

"
def botonabout():
    venab=tk.Tk()
    venab.geometry('800x600')
    venab.title('Sobre este juego')
    info=tk.Label(venab,text=('Informacion Importante'), font= ('Arial',12))
    infor=tk.Label(venab,text= n, font= ('Arial',12))
    info.pack()
    infor.pack()
    venab.mainloop()

