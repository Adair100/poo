class Manejo:

   def metodo(self): #este metodo nos ayudara al poder realizar si se sigue o se cierra el programa
        respuesta = "S"#si la respuesta es s sigue si es n acabara
        while respuesta == "S" or respuesta == "s":#no importa si es minuscula o mayuscula ambos realizaran el mismo trabajo    
            number = 0 #Una de estas vareiables nos ayuda a liminar cualquier valor previo que pudiera existir

            number=int(input("INTRODUCE UN NUMERO: ")) #Se solicita un dato para realizar la convrsion lo caul deberia de ser numero 


            if number%2 == 0: #Esta propiedad se usa lo que es un modeulo para saber si es par o impar
                 print("EL NUMERO: %d ES PAR" %number)  #Si el rsultado es numero 0 es par
            else:
                print("EL NUMERO: %d ES IMPAR" %number)# Si el resultado no es igual es impar
            
            import math 
            nu = number
            print("ESTE ES SU RAIZ CUADRADA:",math.sqrt (nu))# Se calcula lo que es raiz cuadrada

            def raiz (y):#tomara unh numero y calculara su raiz cuadrada
                x = 0

                while nu * nu <= y:# Esto nos ayudara a poder en contra la raiz multiplicando por el mismo numero
                    x += 0.00001
                return nu
            print("ESTE ES EL NUMERO QUE SE ESTA UTILIZANDO:",raiz(nu))#Por parte sera un resultado aplicando sqrt
            
            print("ESTE NUMERO AL CUBO ES:" ,number**3)
            
            
            if respuesta=="n" or respuesta=="N":
                break

objeto = Manejo()
objeto.metodo()