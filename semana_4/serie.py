class Serie: 
    #metodos
    def ver(self):
        print("ver capitulos de la serie")
    
    def opinion(self):
        print("opinion acerca de cada capitulo")
    
    def familiar(self):
        print("observar en familia o sin niños")
    
    def clase(self):
        print("que tipo de clase a b o c")
    
    def tipo(self):
        print("es para jovenes o adultos")

    #atributos
    def trama(self): 
        print("si") 
    def guion(self):
        print("si")
    def tiempo(self): 
        print("160 minutos")
    def tamaño(self):
        print("1 gb")
    def hora(self):
        print("7 pm")
    def capitulos(self):
        print("10")
    def tiempo_por_capitulo(self):
        print("20 minutos")
    def personajes(self):
        print("4")
    def inicio(self):
        print("6 de junio")
    def final(self):
        print("20 de junio")

    #polimorfismo
    def ver(self):
      print("ver los capitulos que llevan")
    
    def opinion(self):
      print("dar opinion sobre el gusto")

    def trama(self):
      print("tiene una buena trama o no es lo mejor")
    
    def guion(self):
      print("tiene un excelente guion por el director")

    def tiempo(self):
      print("tiempo es demasiado o es el mejor")

    def tamaño(self):
      print("si descargas sera de un 1 gb ")

    def hora(self):
      print("la hora de lanzamineto si es acorde al usario")
   
    #herencia
class iron_fist:
    #metodos
    def __init__(self):
      print("Constructor iron fist")
    
    def Ver(self):
        print("ver la serie por capitulos o metodos que ofrce la plataforma")
    
    def Opinion(self):
        print("opinion sobre la temporada de iron fist")
     
     #atributos
    tiempo = "70"
    calidad = "4k"
    actores = "30"
    dirctores = "1"
    carga = "4"

objeto_serie = Serie()
objeto_serie.ver()
objeto_serie.opinion()
objeto_serie.familiar()
objeto_serie.clase()
objeto_serie.tipo()
print("trama = si")
print("guion = si")
print("tiempo = 160")
print("tamaño = 1 gb")
print("hora = 7 pm")
print("capitulos = 10")
print("tiempo por capitulo = 20 minutos")
print("personajes = 4")
print("inicio = 6 de junio")
print("final = 20 d junio")



objeto_serie = iron_fist()
objeto_serie.Ver()
objeto_serie.Opinion()
print("tiempo 70")
print("calidad 4k")
print("actores 30")
print("directores 1")
print("carga  4")

objeto_serie = Serie()
objeto_serie.trama()
objeto_serie.guion()
objeto_serie.tiempo()
objeto_serie.tamaño()
objeto_serie.hora()