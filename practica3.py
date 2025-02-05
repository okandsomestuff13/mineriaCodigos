import random
import matplotlib.pyplot as plt

# Definir el tamaño de la muestra y generar datos aleatorios
muestra = 10
valores = [random.randint(0, 1500) for _ in range(muestra)]

# Definir los intervalos para el histograma
rangos = list(range(0, 1500, 150))
intervalos_histograma = [(rangos[i], rangos[i + 1] - 1) for i in range(len(rangos) - 1)]

# Calcular la frecuencia absoluta para cada intervalo
frecuencia_absoluta = [0] * len(intervalos_histograma)
for valor in valores:
    for indice, (inicio, fin) in enumerate(intervalos_histograma):
        if inicio <= valor <= fin:
            frecuencia_absoluta[indice] += 1
            break

# Calcular la frecuencia relativa
frecuencia_relativa = [fa / muestra for fa in frecuencia_absoluta]

# Mostrar la tabla de frecuencias
print("\nTabla de Frecuencias:")
print("Intervalo     Frecuencia Absoluta   Frecuencia Relativa")
for i in range(len(intervalos_histograma)):
    print(f"[{intervalos_histograma[i][0]}, {intervalos_histograma[i][1]}]  {frecuencia_absoluta[i]}  {frecuencia_relativa[i]}")

# Crear etiquetas para los intervalos
etiquetas_intervalos = [f"[{inicio}, {fin}]" for inicio, fin in intervalos_histograma]

# Graficar el histograma
plt.figure(figsize=(10, 5))
plt.bar(etiquetas_intervalos, frecuencia_absoluta, color='lightgreen', edgecolor='black')

plt.xlabel("Intervalos")
plt.ylabel("Frecuencia Absoluta")
plt.title("Distribución de Datos - Histograma")
plt.xticks(rotation=45)  
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.show()
