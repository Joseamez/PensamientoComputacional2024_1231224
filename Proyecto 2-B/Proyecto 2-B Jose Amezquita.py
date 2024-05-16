import datetime  # Importamos el módulo datetime

# Diccionario para almacenar las zonas y temperaturas
zonas = {}

# Diccionario para almacenar los horarios programados
horarios = {}

# Temperatura por defecto para las zonas
TEMP_DEFECTO = 22.0

# Función para configurar las zonas de temperatura iniciales
def configurar_zonas_iniciales():
    num_zonas = int(input("Ingrese el número de zonas: "))
    for i in range(num_zonas):
        nombre_zona = input(f"Ingrese el nombre de la zona {i+1}: ")
        zonas[nombre_zona] = TEMP_DEFECTO
    print("Zonas configuradas correctamente con temperatura por defecto de 22°C.")

# Función para configurar las zonas de temperatura
def configurar_zonas():
    while True:
        opcion = input("¿Desea añadir una nueva zona, eliminar una zona existente o salir? (escriba añadir o eliminar) ").lower()
        if opcion == "añadir":
            nombre_zona = input("Ingrese el nombre de la nueva zona: ")
            if nombre_zona in zonas:
                print(f"La zona '{nombre_zona}' ya existe.")
            else:
                zonas[nombre_zona] = TEMP_DEFECTO
                print(f"La zona '{nombre_zona}' ha sido agregada con temperatura por defecto de 22°C.")
        elif opcion == "eliminar":
            print("Zonas configuradas:")
            for zona in zonas:
                print(f"- {zona}")

            zona_eliminar = input("Ingrese el nombre de la zona que desea eliminar: ")
            if zona_eliminar in zonas:
                del zonas[zona_eliminar]
                print(f"La zona '{zona_eliminar}' ha sido eliminada.")

                # Eliminar los horarios programados para la zona eliminada
                horarios_eliminar = [(zona, inicio, fin) for (zona, inicio, fin) in horarios if zona == zona_eliminar]
                for horario in horarios_eliminar:
                    del horarios[horario]
                    print(f"Horario {horario[1]} - {horario[2]} eliminado para la zona '{zona_eliminar}'.")
            else:
                print(f"La zona '{zona_eliminar}' no existe.")
        elif opcion == "salir":
            break
        else:
            print("Opción inválida.")

# Función para controlar la temperatura por zonas
def controlar_temperatura():
    print("Zonas configuradas:")
    for zona, temp in zonas.items():
        print(f"{zona}: {temp}°C")

    zona_seleccionada = input("Ingrese el nombre de la zona que desea ajustar: ")
    if zona_seleccionada in zonas:
        nueva_temp = float(input(f"Ingrese la nueva temperatura deseada para la zona '{zona_seleccionada}': "))
        zonas[zona_seleccionada] = nueva_temp
        print(f"Temperatura actualizada para la zona '{zona_seleccionada}': {nueva_temp}°C")
    else:
        print("La zona ingresada no existe.")

# Función para programar horarios
def programar_horarios():
    hora_actual = datetime.datetime.now().strftime("%H:%M")
    print(f"Hora actual del sistema: {hora_actual}")

    zona_seleccionada = input("Ingrese el nombre de la zona para programar horarios: ")
    if zona_seleccionada in zonas:
        opcion = input("¿Desea programar un nuevo horario o eliminar un horario existente? (escria programar nuevo o eliminar) ").lower()
        if opcion == "programar nuevo":
            horario_inicio = input("Ingrese la hora de inicio (HH:MM): ")
            horario_fin = input("Ingrese la hora de fin (HH:MM): ")
            temp_deseada = float(input(f"Ingrese la temperatura deseada para la zona '{zona_seleccionada}' durante ese horario: "))
            horarios[(zona_seleccionada, horario_inicio, horario_fin)] = temp_deseada
            print("Horario programado correctamente.")
        elif opcion == "eliminar":
            print("Horarios programados para la zona seleccionada:")
            horarios_zona = [(inicio, fin, temp) for (zona, inicio, fin), temp in horarios.items() if zona == zona_seleccionada]
            for i, (inicio, fin, temp) in enumerate(horarios_zona, start=1):
                print(f"{i}. {inicio} - {fin}: {temp}°C")

            if horarios_zona:
                seleccion = int(input("Ingrese el número del horario que desea eliminar: "))
                if 1 <= seleccion <= len(horarios_zona):
                    horario_eliminar = (zona_seleccionada, horarios_zona[seleccion-1][0], horarios_zona[seleccion-1][1])
                    del horarios[horario_eliminar]
                    print("Horario eliminado correctamente.")
                else:
                    print("Selección inválida.")
            else:
                print("No hay horarios programados para esta zona.")
        else:
            print("Opción inválida.")
    else:
        print("La zona ingresada no existe.")

# Función para simular los sensores de temperatura
def sensores_temperatura():
    hora_actual = datetime.datetime.now().strftime("%H:%M")
    print(f"Hora actual del sistema: {hora_actual}")

    print("Temperaturas actuales:")
    for zona, temp_deseada in zonas.items():
        temp_actual = temp_deseada  # Simulación de temperatura actual

        # Verificar horarios programados
        for horario, temp_programada in horarios.items():
            zona_horario, inicio, fin = horario
            if zona_horario == zona and inicio <= hora_actual <= fin:
                temp_actual = temp_programada
                print(f"{zona}: {temp_actual}°C (Programado)")
                break
        else:
            print(f"{zona}: {temp_actual}°C")

# Función para optimizar el consumo energético
def optimizacion_energetica():
    temp_minima = float(input("Ingrese la temperatura mínima del rango: "))
    temp_maxima = float(input("Ingrese la temperatura máxima del rango: "))

    for zona, temp in zonas.items():
        if temp < temp_minima or temp > temp_maxima:
            print(f"La zona '{zona}' está fuera del rango de temperatura ({temp_minima}°C - {temp_maxima}°C). Ajustando a 22°C.")
            zonas[zona] = TEMP_DEFECTO

# Menú principal
def menu_principal():
    while True:
        print("\nMenú Principal")
        print("1. Configurar zonas")
        print("2. Controlar temperatura por zonas")
        print("3. Programar horarios")
        print("4. Sensores de temperatura")
        print("5. Optimización energética")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            configurar_zonas()
        elif opcion == "2":
            controlar_temperatura()
        elif opcion == "3":
            programar_horarios()
        elif opcion == "4":
            sensores_temperatura()
        elif opcion == "5":
            optimizacion_energetica()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Iniciar el programa
configurar_zonas_iniciales()
menu_principal()

