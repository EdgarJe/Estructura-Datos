import random
import numpy as np

def GenerarMatriz():
    filas = int(input(f"Numero de filas: "))
    columnas = int(input(f"Numero de columnas: "))
    matriz = random.randint(-100, 101, size=(filas, columnas))
    return matriz

def MostrarMatriz(matriz, nombre):
    print(f"\nMatriz {nombre}:")
    print(matriz)

def Menu():
    matriz_A = None
    matriz_B = None
    matriz_C = None
    
    while True:
        print("\nSeleccione una opción:")
        print("1. Crear una matriz A con valores aleatorios del -100 al 100")
        print("2. Crear una matriz B con valores aleatorios del -100 al 100")
        print("3. Realizar C = A + B")
        print("4. Realizar C = A - B")
        print("5. Mostrar matrices A, B, o C")
        print("6. Salir")
    
        opcion = input("Ingrese su opción: ")
    
        if opcion == "1":
            matriz_A = GenerarMatriz("A")
        elif opcion == "2":
            matriz_B = GenerarMatriz("B")
        elif opcion == "3":
            if matriz_A is not None and matriz_B is not None:
                matriz_C = matriz_A + matriz_B
                print("\nSe realizó la operación C = A + B")
            else:
                print("Debe crear primero las matrices A y B.")
        elif opcion == "4":
            if matriz_A is not None and matriz_B is not None:
                matriz_C = matriz_A - matriz_B
                print("\nSe realizó la operación C = A - B")
            else:
                print("Debe crear primero las matrices A y B.")
        elif opcion == "5":
            if matriz_A is not None:
                MostrarMatriz(matriz_A, "A")
            if matriz_B is not None:
                MostrarMatriz(matriz_B, "B")
            if matriz_C is not None:
                MostrarMatriz(matriz_C, "C")
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")



Menu()