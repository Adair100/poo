class Futbolista :
    #metodos
    def patear(self):
        print("patea a la porteria")
    
    def correr (self):
        print("correr en distintas partes de la cancha")
   
    def trotar(self):
        print("trota a una velocidad especifica")
    
    def estiramiento (self):
        print("sus musculos evita algo a lastimar")

    def hidratacion(self):
        print("evita tener cansacion rapido")
    
    
    
   #atributos
    def talla(self):  
        print("11")

    def goles(self):
        print("80")

    def peso(self): 
        print("58")

    def litro(self): 
        print("20")

    def edad(self): 
        print("20")

    def altura(self): 
        print("1.80")

    def numero_pie(self): 
        print("28")

    def numero_cancha(self):
        print("7")

    def tarjetas(self): 
        print("8")

    def expulsions(self):
        print("8")


   #herencia
  
class cr7:
    #metodos
    def __init__(self):
      print("Constructor cr7")

    def Correr(self):
      print("tener que evitar un gol")
    
    def patear(self):
      print("tener mayor goles en un partido")

    #atributos
    correr = "10"
    trotar = "10"
    caminar = "10"
    peso = "60"
    altura = "1.77"


objeto_futbolista = Futbolista()
objeto_futbolista.patear()
objeto_futbolista.correr()
objeto_futbolista.trotar()
objeto_futbolista.estiramiento()
objeto_futbolista.hidratacion()
print("talla = 11")
print("goles = 80")
print("peso = 58")
print("litro = 20")
print("edad = 20")
print("altura = 1.80")
print("numero_pie = 28")
print("numero_cancha = 7")
print("tarjetas = 8")
print("expulsiones = 8")



objeto_futbolista = cr7()
objeto_futbolista.Correr()
objeto_futbolista.patear()
print("correr 10")
print("trotar 10")
print("caminar 10")
print("peso 60")
print("altura 1.77")

objeto_futbolista = Futbolista()
objeto_futbolista.talla()
objeto_futbolista.goles()
objeto_futbolista.peso()
objeto_futbolista.litro()
objeto_futbolista.edad()