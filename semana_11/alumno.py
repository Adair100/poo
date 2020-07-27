class alumno:#iniciiamos con la clase para poder tener el codigo medinate objetos
   def metodo(self): #este metodo nos ayudara al poder realizar si se sigue o se cierra el programa
        respuesta = "S"#si la respuesta es s sigue si es n acabara
        while respuesta == "S" or respuesta == "s":#no importa si es minuscula o matuscula ambos realizaran el mismo trabajo

            alumn = input("¿Cual es tu nombre?:")#input nos ayuda a leer el valor y tenerlo en texto
            print(alumn)#print mostrara lo que se guardo en la variable alumn
  
            edad = int(input("¿Cual es tu edad?:"))#int input nos ayudara a la conversion de textoa numero entero 
            print(edad, alumn)#print nos dara lo que se guardo en la variable edad pero tambien en alumn

            respuesta = input("¿desea realizar otra conversion S/N?:")#si la respuesta en n se c errara el programa
            if respuesta=="n" or respuesta=="N":
                break



alumno = alumno()#ayuda a llamar el objeto lo cual iniciamos con la clase alumno
alumno.metodo()#esto nos ayuda a poder seguir con el metodo y poder tener el programa visible