#Aqui en el main primero pues importamos el módulo de modelos.py que hice
from modelos import Creditos, Cancion, MusicaExclusiva #<- Aqui estan todos los metodos que cree

# 1. Objetos aqui se ve la compocisión Creditos y la clase padre Cancion
creditos_1 = Creditos("Parlophone UK", "Coldplay")
Cancion_1 = Cancion(
    creditos_1,
    "Sparks",
    3,
    "Parachutes"
)

Cancion_1.reproducir_cancion()
Cancion_1.minutos_escuchados(10)
Cancion_1.informacion_cancion()  # <- Aqui vemos si realmente hace bien su trabajo de compocision ya que se va a creditos_1.obtener_detalle_creditos()
Cancion_1.favorita(False)

#Aqui hicimos las funciones de ENCAPSULAMIENTO
print(f"Consulta segura con Getter: {Cancion_1.reproducciones} reproducciones") #Se ve que el getter funciona de manera correcta
Cancion_1.reproducciones = 25 # Usamos el setter para darle un nuevo valor de forma válida
print(f"Nuevo valor asignado con Setter: {Cancion_1.reproducciones} reproducciones")  #El print del nuevo valor que se le asigno

#En esta parte instanciamos un objeto 'Cancion_2' haciendo que todo se valide correctamente, aplicando el polimorfismo
print("---------------------------")
creditos_2 = Creditos("WM Mexico", "Maná")
Cancion_2 = MusicaExclusiva(
    creditos_2,
    "Labios Compartidos",
    5,
    "Amar Es Combatir",
    plan_suscripcion="Premium",
    region="MX"
)

Cancion_2.reproducir_cancion()
Cancion_2.descargar_musica()
Cancion_2.informacion_cancion()
Cancion_2.favorita(True)

#En esta parte instanciamos un objeto 'Cancion_3' haciendo que sea una prueba de validacion incorrecta, aplicando el polimorfismo
print("---------------------------")
creditos_3 = Creditos("Musart-Balboa", "Joan Sebastian")
Cancion_3 = MusicaExclusiva(
    creditos_3,
    "Eso y Más (Inedita)",
    2,
    "Más alla del sol",
    plan_suscripcion="Gratuito",
    region="USA"
)

Cancion_3.reproducir_cancion()
Cancion_3.descargar_musica()
Cancion_3.informacion_cancion()
print("---------------------------")

#Brian Cayetano Martínez
