#Prblema 1

def obtener_mayor(precios):
    mayor = precios[0]
    for precio in precios:
        if precio > mayor:
            mayor = precio
    return mayor
def obtener_menor(precios):
    menor = precios[0]
    for precio in precios:
        if precio < menor:
            menor = precio
    return menor
precios = [50, 75, 46, 22, 80, 65, 8]
precio_mayor = obtener_mayor(precios)
precio_menor = obtener_menor(precios)
print("El precio mayor es:", precio_mayor)
print("El precio menor es:", precio_menor)


#Problema 2

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
indice = 2 
while indice < len(abc):
    abc.pop(indice)
    indice += 2  
print("La lista resultante es:")
print(abc)


#Problema 3

word = ["pantufla", "agua", "mesa", "pantufla", "rojo", "pantufla", "lobo"]
word_buscada = input("Ingresa una palabra: ")
contador = word.count(word_buscada)
print(f"La palabra '{word_buscada}' aparece {contador} veces en la lista.")