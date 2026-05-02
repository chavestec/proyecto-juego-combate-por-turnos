import csv
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

cargar_personajes()
print(personajes)
