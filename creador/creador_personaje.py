import uuid
import json
import time
from pj import personajes

data = {}
data['personajes_creados'] = []
class Personaje():

    def __init__(self, nombre, raza, clase, vida, mana):
        self.nombre = nombre
        self.raza = raza
        self.clase = clase
        self.vida = vida
        self.mana = mana

    def configurarPersonaje(self):
        print("""\n ¿Qué personaje deseas crear?\n
        1) Humanos
        2) Orcos""")
        raza_seleccionada = input("\n> ")

        if raza_seleccionada == '1':
            raza_seleccionada = "Humanos"
            print("""\n¿Qué clase de humano deseas crear?\n
            1) Guerrero
            2) Jinete
            3) Mago """)

            clase_seleccionada = input("\n>")
            if clase_seleccionada == '1':
                clase_seleccionada = 'Guerrero'
                self.crearPersonaje(raza_seleccionada, clase_seleccionada)
            elif clase_seleccionada == '2':
                clase_seleccionada = 'Jinete'
                self.crearPersonaje(raza_seleccionada, clase_seleccionada)
            elif clase_seleccionada == '3':
                clase_seleccionada = 'Mago'
                self.crearPersonaje(raza_seleccionada, clase_seleccionada)
        elif raza_seleccionada == '2':
            raza_seleccionada = "Orcos"
            print("""\n¿Qué clase de orco deseas crear?\n
            1) Guerrero
            2) Chamán
            3) Jinete """)

            clase_seleccionada = input("\n> ")
            if clase_seleccionada == '1':
                clase_seleccionada = 'Guerrero'
                self.crearPersonaje(raza_seleccionada, clase_seleccionada)
            elif clase_seleccionada == '2':
                clase_seleccionada = 'Chamán'
                self.crearPersonaje(raza_seleccionada, clase_seleccionada)
            elif clase_seleccionada == '3':
                clase_seleccionada = 'Jinete'
                self.crearPersonaje(raza_seleccionada, clase_seleccionada)
        else:
            print("\nHas introducido un comando inválido")


    def crearPersonaje(self, raza_seleccionada, clase_seleccionada):
        vida = personajes['Raza'][raza_seleccionada]['Clase'][clase_seleccionada]['Stats']['Vida']
        mana = personajes['Raza'][raza_seleccionada]['Clase'][clase_seleccionada]['Stats']['Mana']

        nombre = input("\nIntroduce el nombre de tu personaje > ")
        
        nuevo_pj = Personaje(
            nombre=nombre, raza=raza_seleccionada, clase=clase_seleccionada, vida=vida, mana=mana)
        datos = {
            "id": str(uuid.uuid4()),
            "Nombre": nuevo_pj.nombre,
            "Raza": nuevo_pj.raza,
            "Clase": nuevo_pj.clase,
            "Vida": nuevo_pj.vida,
            "Mana": nuevo_pj.mana
        }
        print("\nEl personaje \"{}\" ha sido creado".format(datos["Nombre"]))
        self.guardarPersonaje(datos)


    def guardarPersonaje(self, datos):
        data['personajes_creados'].append(datos)
        pjs = data['personajes_creados']
        archivo = open('Personajes.json', 'w')
        json.dump(pjs, archivo, indent=4)

    def cargarPersonajes(self):
        try:
            archivo = open('Personajes.json')
            data['personajes_creados'] = json.load(archivo)
        except FileNotFoundError:
            print("\nCreando registro de personajes...")
            time.sleep(1)
            archivo = open('Personajes.json', 'a+')
        except json.decoder.JSONDecodeError:
            print("\nNo hay personajes creados, crea nuevos personajes a partir de ahora;D")

    def interfaz(self):
        i = 0
        while True:
            print("""\n=== Bienvenido al creador de personajes humanos y orcos ===\n
                ¿Qué deseas hacer?\n
                1) Crear un personaje
                2) Ver los personajes creados
                3) Salir del programa\n""")
            opcion = input("> ")
            if opcion == '1':
                self.configurarPersonaje()
            elif opcion == '2':
                if data['personajes_creados'] == []:
                    print("\nNo se encuentran personajes registrados")
                for personaje in data['personajes_creados']:
                    print("""\nID: {}
                        Nombre: {}
                        Raza: {}
                        Clase: {}
                        Vida: {}
                        Mana: {}\n """.format(personaje['id'], personaje['Nombre'], personaje['Raza'], personaje['Clase'],
                        personaje['Vida'], personaje['Mana']))
            elif opcion == '3':
                print("\nGracias por usar el programa;)")
                time.sleep(2)
                quit()
            else:
                print("\nHas introducido un comando inválido")


class Iniciar(Personaje):
    def __init__(self):
        self.cargarPersonajes()
        self.interfaz()


Iniciar()
print(data['personajes_creados'])
