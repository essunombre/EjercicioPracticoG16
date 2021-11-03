# este archivo es solo para probar la libreria procesador_texto.py
import say_hi as sh
import procesador_texto as pt



print("CONTAR CARACTERES")
cad = input("Digita el texto: ")
num_car = pt.contar_caracteres(cad)
print(num_car, "caracteres en", cad)

#Funcion saludar Jose
print("Say hi:")
nombre = input("Ingresa nombre:")
hola = sh.say_hi(nombre)

