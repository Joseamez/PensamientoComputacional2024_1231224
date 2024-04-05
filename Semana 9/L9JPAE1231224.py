#ejercicio 1
print("hola, dame tu edad")
edad=int(input())
if edad >= 18:
    print("ya sos mayor, tramita DPI, tenes")
else:
    print("No sos mayor de edad, vete")



#ejercicio 2
print("hola, dame un numero positivo o negativo")
num=int(input())
if num >= 0:
    print(" definitivamente tu numero es positivo")
else:
    print("tu numero es negativo bro")


#ejercicio 3
def numero_a_letras(numero): 
    match = { 
        1: "uno", 
        2: "dos", 
        3: "tres", 
        4: "cuatro", 
        5: "cinco" 
   } 
    return match.get(numero, "número no definido") 
numero = int(input("Ingrese un número del 1 al 5: ")) 
if 1 <= numero <= 5:
    print(numero_a_letras(numero)) 
else: print("número no definido")

#ejercicio 4
rint("Esta es la tabla del 2")
cont= 0
while cont <= 5:
    x= cont*2
    print(x)
    cont= cont+1
print("Es esa") 