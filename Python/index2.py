import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')


ax = df['Cantidad de ventas bruto'].plot(kind='bar')


total_ventas = df['Cantidad de ventas bruto'].sum()
title = "Total Ventas: ${:,.2f}".format(total_ventas)
plt.title(title)


for i, val in enumerate(df['Cantidad de ventas bruto']):
    if val != 0:
        plt.text(i-0.3, val+10, "${:,.2f}".format(val), color='black', rotation=0, ha='center')


periodos = list(df.index + 1) 
plt.xticks(range(len(periodos)), periodos)

plt.show()