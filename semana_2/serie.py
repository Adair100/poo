class serieTV:

    #MÉTODOS

    def Tiempo(self):
        print("tiempo de duracion de la serie")
    
    def disfrutar(self):
        print("disfrutar de cada capitulo de la serie")
    
    def relajar(self):
        print("relajar ayuda para que tengas una mejor experiencia de la serie")

    def emociones(self):
        print("emociones que genera la serie")
    
    def temporadas(self):
        print("temporadas que maneja la serie")

    #ATRIBUTOS
    tiempo = " "
    tamaño = " "
    actores = " "
    directores = " "
    guion = " "
    capitulos = " "
    fecha = " "
    intro =" "
    precio = " "
    descarga = " "
       


serie_netflix = serieTV()

 #METODOS

serie_netflix.Tiempo()
serie_netflix.disfrutar()
serie_netflix.relajar()
serie_netflix.emociones()
serie_netflix.temporadas()


 #ATRIBUTOS

serie_netflix.tiempo  = "120 minutos "
serie_netflix.tamaño  = "4 gb por toda la serie"
serie_netflix.actores  = "cada actor tiene su papel en la tv"
serie_netflix.directores  = "2 que manejan parte de la serie"
serie_netflix.guion  = "guion de la serie para cada actor "
serie_netflix.capitulos  = "40 capitulos"
serie_netflix.fecha  = "2 de marzo inicio de la serie"
serie_netflix.intro  = "una cancion relacionada a la serie"
serie_netflix.precio  = "gratias 2 temporadas y el resto der pago de $100.00"
serie_netflix.descarga  = "mediante netflix "

print(serie_netflix.tiempo )
print(serie_netflix.tamaño )
print(serie_netflix.actores )
print(serie_netflix.directores )
print(serie_netflix.guion )
print(serie_netflix.capitulos )
print(serie_netflix.fecha )
print(serie_netflix.intro )
print(serie_netflix.precio )
print(serie_netflix.descarga )