class diccionario:

   def metodo(self): #este metodo nos ayudara al poder realizar si se sigue o se cierra el programa
        respuesta = "S"#si la respuesta es s sigue si es n acabara
        while respuesta == "S" or respuesta == "s":#no importa si es minuscula o matuscula ambos realizaran el mismo trabajo    
            pelicula = input("¿Cual es tu nombre de tu pelicula?:")#input nos ayuda a leer el valor y tenerlo en texto
            print("Pelicula: ",pelicula)#print mostrara lo que se guardo en la variable pelicula
  
            genero = input("¿Cual es el genero de la pelicula?:")# input nos ayudara a poder tener el texto y escribir solamente letras 
            print("Genero: ", genero)#print nos dara lo que se guardo en la variable genero

            año = int(input("¿Cual es año de lanzamiento de la pelicula?:"))#int input nos ayudara a la conversion de texto a numero entero 
            print("Año: ", año)#print nos dara lo que se guardo en la variable edad pero tambien en año

            respuesta = input("¿desea realizar otra pelicula S/N?:")#si la respuesta en n se cerrara el programa
            if respuesta=="n" or respuesta=="N":
                break
          
objeto = diccionario()
objeto.metodo()