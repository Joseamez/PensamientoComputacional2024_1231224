def tipo_triangulo(a, b, c):
    if a == b == c:
        return "Equilátero"
    elif a == b or a == c or b == c:
    else:
        return "Escaleno"

def main():
    l1 = float(input("Ingrese la longitud del primer lado del triángulo: "))
    l2 = float(input("Ingrese la longitud del segundo lado del triángulo: "))
    l3 = float(input("Ingrese la longitud del tercer lado del triángulo: "))

    tipo = tipo_triangulo(l1, l2, l3)
    print("El triángulo es:", tipo)

if __name__ == "__main__":
    main()


#ejercicio 2

import math

def ObtenerPerimetro(radio): 
    perimetro = 2 * math.pi * radio 
    return perimetro 

def ObtenerArea(radio): 
    area = math.pi * radio**2 
    return area 

def ObtenerVolumen(radio): 
    volumen = (4/3) * math.pi * radio**3 
    return volumen 

radio = float(input("Ingrese el radio del círculo: ")) 
perimetro = ObtenerPerimetro(radio)
area = ObtenerArea(radio)
volumen = ObtenerVolumen(radio)

print(f"El perímetro del círculo es: {perimetro:.2f}") 
print(f"El área del círculo es: {area:.2f}") 
print(f"El volumen de la esfera es: {volumen:.2f}")

#Ejercicio3

def imprimir_nombre_mes(numero):
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    if numero in meses:
        print(meses[numero])
    else:
        print("Número no válido. Debe ser un número del 1 al 12.")

numero_mes_str = input("Ingrese un número del 1 al 12: ")


try:
    numero_mes = int(numero_mes_str)

    imprimir_nombre_mes(numero_mes)
except ValueError:

    print("Entrada no válida. Debe ingresar un número del 1 al 12.")
