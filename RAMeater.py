import random
import pandas as pd

# Función para generar la matriz de 1000 alumnos y 500 materias
def generar_matriz():
    # Crear una lista para almacenar los datos de los alumnos
    alumnos = []
    
    # Crear 1000 alumnos con sus calificaciones en 500 materias
    for i in range(1, 10001):
        alumno = {
            "ID Alumno": i,
        }
        
        # Asignar calificaciones aleatorias entre 0 y 10 para cada una de las 500 materias
        for materia in range(1, 501):
            alumno[f"Materia {materia}"] = random.randint(0, 10)
        
        alumnos.append(alumno)
    
    # Crear un DataFrame (tabla) usando pandas
    df = pd.DataFrame(alumnos)
    return df

# Función para buscar un alumno por ID
def buscar_alumno(df, id_alumno):
    alumno = df[df["ID Alumno"] == id_alumno]
    if not alumno.empty:
        return alumno
    else:
        return f"Alumno con ID {id_alumno} no encontrado."

# Función para buscar las calificaciones de la materia 5
def buscar_materia(df, materia_index):
    if materia_index < 1 or materia_index > 500:
        return "El índice de la materia debe estar entre 1 y 500."
    
    materia = f"Materia {materia_index}"  # Nombre de la materia correspondiente
    notas_materia = df[["ID Alumno", materia]]
    return notas_materia

# Función principal
def main():
    # Generar la matriz (tabla) con 1000 alumnos y 500 materias
    df = generar_matriz()
    
    # Establecer opciones de pandas para que no recorte las filas ni las columnas
    pd.set_option('display.max_rows', None)  # Mostrar todas las filas
    pd.set_option('display.max_columns', None)  # Mostrar todas las columnas
    pd.set_option('display.width', None)  # Ajustar el ancho para que no se corte la tabla
    pd.set_option('display.max_colwidth', None)  # Mostrar todo el contenido de las celdas
    
    # Mostrar la tabla de alumnos y calificaciones
    print("Tabla de Alumnos y Calificaciones en 500 Materias:")
    print(df)

    # Buscar al alumno con ID 321
    id_alumno_buscar = 321
    alumno = buscar_alumno(df, id_alumno_buscar)
    print("\nBúsqueda del Alumno con ID 321:")
    print(alumno)

    # Buscar las notas de la materia 5
    materia_buscar = 5
    notas_materia = buscar_materia(df, materia_buscar)
    print(f"\nNotas de la Materia {materia_buscar}:")
    print(notas_materia)

# Ejecutar el programa
if __name__ == "__main__":
    main()
