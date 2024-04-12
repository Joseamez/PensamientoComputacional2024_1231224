#ejercicio 1
numero = int(input("Por favor ingresa un número: "))

print("Tabla de multiplicar del", numero)
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)


#ejercicio 2
def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

numero = int(input("Ingrese un número: "))

if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")

#ejercicio 3
def suma_hasta_n(numero):
    suma_total = 0
    for i in range(1, numero + 1):
        suma_total += i
    return suma_total

def main():
    numero = int(input("Ingresa un número: "))
    total = suma_hasta_n(numero)
    print("La suma desde 1 hasta", numero, "es:", total)

if __name__ == "__main__":
    main()
