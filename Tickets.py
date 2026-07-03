import random

def sistema_tickets():
    # Lista para almacenar todos los tickets creados
    base_de_datos = {}
    
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Alta ticket")
        print("2. Leer ticket")
        print("3. Salir")
        
        opcion = input("Seleccione una opción (1-3): ")
        
        # --- ALTA TICKET ---
        if opcion == "1":
            while True:
                print("\n--- NUEVO TICKET ---")
                nombre = input("Nombre: ")
                sector = input("Sector: ")
                asunto = input("Asunto: ")
                problema = input("Problema: ")
                
                # Generar número random
                num_ticket = random.randint(1000, 9999)
                
                # Guardar en el diccionario
                ticket = {
                    "nombre": nombre,
                    "sector": sector,
                    "asunto": asunto,
                    "problema": problema
                }
                base_de_datos[num_ticket] = ticket
                
                # Mostrar ticket
                print(f"\n--- TICKET CREADO ---")
                print(f"Número de ticket: {num_ticket}")
                print(f"Nombre: {nombre} | Sector: {sector}")
                print(f"Asunto: {asunto}")
                print(f"Problema: {problema}")
                print("¡IMPORTANTE! Recuerde su número de ticket.")
                
                continuar = input("\n¿Desea crear otro ticket? (s/n): ").lower()
                if continuar != 's':
                    break
        
        # --- LEER TICKET ---
        elif opcion == "2":
            while True:
                try:
                    buscar = int(input("\nIngrese el número de ticket a consultar: "))
                    if buscar in base_de_datos:
                        t = base_de_datos[buscar]
                        print(f"\n--- DETALLE DEL TICKET {buscar} ---")
                        print(f"Nombre: {t['nombre']} | Sector: {t['sector']}")
                        print(f"Asunto: {t['asunto']}")
                        print(f"Problema: {t['problema']}")
                    else:
                        print("Error: Ticket no encontrado.")
                except ValueError:
                    print("Por favor, ingrese un número válido.")
                
                continuar = input("\n¿Desea consultar otro ticket? (s/n): ").lower()
                if continuar != 's':
                    break
        
        # --- SALIR ---
        elif opcion == "3":
            confirmar = input("¿Está seguro que desea salir? (s/n): ").lower()
            if confirmar == 's':
                print("Cerrando programa. ¡Adiós!")
                break
        
        else:
            print("Opción no válida, intente nuevamente.")

# Ejecutar el programa
sistema_tickets()