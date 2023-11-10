import numpy as np
from datasets import load_dataset

# Cargar el conjunto de datos
dataset = load_dataset("mstz/heart_failure")
data = dataset["train"]

# Obtener la lista de edades
edades = data["age"]

# Convertir la lista de edades a un arreglo de NumPy
edades_np = np.array(edades)

# Calcular el promedio de edad
promedio_edad = np.mean(edades_np)

# Imprimir el resultado
print(f"El promedio de edad de las personas participantes en el estudio es: {promedio_edad} años")
