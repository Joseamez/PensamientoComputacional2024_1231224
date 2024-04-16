#Diccionario para contar los boletos vendidos
boletos_vendidos = {}

# Función para generar reportes
def generar_reportes(boletos_vendidos):
    print("Reporte de boletos vendidos:")
    for ruta, cantidad in boletos_vendidos.items():
        print(f"Ruta {estaciones[ruta[0]]} - {estaciones[ruta[1]]}: {cantidad} boletos")
    total_boletos = sum(boletos_vendidos.values())
    total_dinero = sum([precio * cantidad for (ruta, precio), cantidad in boletos_vendidos.items()])
    print("Total de boletos vendidos:" + str(total_boletos))
    print("Dinero total percibido: Q" + str(total_dinero))

# Definición de estaciones y rutas
estaciones = {
    51: "Estación Javier",
    61: "Estación Trébol",
    71: "Estación Don Bosco",
    82: "Estación Plaza Municipal"
}

rutas = {
    (51, 61): 39,
    (51, 71): 18,
    (71, 82): 23,
    (61, 51): 8,
    (82, 51): 42
}
    
while True:
        print("\nMenú:")
        print("1. Ver estaciones existentes")
        print("2. Comprar boleto")
        print("3. Generar reportes")
        print("4. Salir")
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            print("Estaciones existentes y rutas disponibles:")
            for codigo, nombre in estaciones.items():
                print(f"Código: {codigo}, Nombre: {nombre}")

        elif opcion == 2:
            print("Compra de boleto:")
            partida = int(input("Ingrese el código de la estación de partida: "))
            destino = int(input("Ingrese el código de la estación de destino: "))
            while (partida, destino) not in rutas:
                print("La ruta ingresada no existe. Por favor, ingrese una ruta válida.")
                partida = int(input("Ingrese el código de la estación de partida: "))
                destino = int(input("Ingrese el código de la estación de destino: "))

            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            embarazada = input("¿Está embarazada? (s/n): ").lower() == 's'

            distancia = rutas[(partida, destino)]
            precio = 1.5 * min(8, distancia) + 0.25 * max(0, distancia - 8)
            if edad >= 15 and edad <= 25:
                precio *= 0.75
            if embarazada:
                precio = 0

            tiempo_viaje = distancia / 20

            print("\nDetalle del boleto:")
            print(f"Estación de partida: {estaciones[partida]}")
            print(f"Estación de destino: {estaciones[destino]}")
            print(f"Precio del boleto: Q{precio:.2f}")
            print(f"Tiempo estimado de viaje: {tiempo_viaje:.2f} horas")
            ruta = (partida, destino)
            boletos_vendidos[ruta] = boletos_vendidos.get(ruta, 0) + 1

        elif opcion == 3:
            generar_reportes(boletos_vendidos)

        elif opcion == 4:
            print("¡Gracias por utilizar el sistema de compra de boletos del Transmetro!")
            break

        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")