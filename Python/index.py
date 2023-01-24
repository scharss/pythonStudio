import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

# Gráfico de barras de la columna 'Cantidad de ventas bruto'
ax = df['Cantidad de ventas bruto'].plot(kind='bar')

# Agregar título al gráfico con el total de ventas
total_ventas = df['Cantidad de ventas bruto'].sum()
title = "Total Ventas: ${:,.2f}".format(total_ventas)
plt.title(title)

# Mostrar valor vendido sobre cada barra
for i, val in enumerate(df['Cantidad de ventas bruto']):
    if val != 0:
        plt.text(i-0.3, val+10, "${:,.2f}".format(val), color='black', rotation=0, ha='center')

# Especificar valores del eje x
periodos = list(df.index + 1) # Agregar 1 para comenzar en 1 en lugar de 0
plt.xticks(range(len(periodos)), periodos)

plt.show()