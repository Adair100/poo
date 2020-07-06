class Conversor:
    def __init__(self, grados):
        self.grados=grados

#linea 6 opcion convierte con la formula para celsius a fahrenheit lo cual con la primer valor realiza la conversion
    def celsius_a_fahrenheit(self,):
        c=input("¿Cual es el valor a convertir?")
        print(c, "En grados celsius:")
        print(float(c)*9/5+32.15, "grados fahrenheit")
#linea 11 realiza diferente formula para conversion de celsius
    def fahrenheit_a_celsius(self,):
        f=input("¿Cual es el valor a convertir?")
        print(f, "En grados fahrenheit")
        c=float(f)-32
        print(float(c)*5/9, "grados celsius")


temperatura = Conversor("")

x=0
#linea 23 desea con el menu que tipo de conversion se necesite ya sea 1 o 2 
while x!=8:
    print("Elige que es lo que desea convertir ¿1 o 2?")

    print("1:Convertidor de Celsius a fahrenheit")
    print("2:Cconvertidor de fahrenheit a celsius")

#linea 29 ya un numero que se eligio va a realizar la formula con el valor dado
    op=input("¿Que numero va a elegir?:")

    if op=="1" or op=="celsius a fahrenheit":
        temperatura.celsius_a_fahrenheit()
    elif op=="2" or op=="fahrenheit a celsius":
        temperatura.fahrenheit_a_celsius()   
    op=input("¿desea realizar otra conversion S/N?:")
    if op=="s" or op=="S":
        x=9
#ultima linea ayuda para dar o pedir si se mecesita realizar otra conversion lo cual en caso de que sea  N se cierra el programa
from io import open 
temperatura=open("temperatura.txt","w")
frase="fahrenheit_a_celsius"
temperatura.write(frase)