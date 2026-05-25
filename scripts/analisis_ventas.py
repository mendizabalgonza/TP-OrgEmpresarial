# analisis_ventas.py
# Descripcion: Script de analisis de ventas simuladas
# Rol: Paco (P2) - Desarrollador Tecnico
# Jira: CD-2

import pandas as pd
import matplotlib.pyplot as plt

# Cargamos el dataset desde /datos usando ruta relativa
df = pd.read_csv('datos/ventas.csv')

# Calculamos el ingreso total por registro
df['total_venta'] = df['cantidad'] * df['precio_unitario']

# Convertimos fecha a datetime para agrupar por mes
df['fecha'] = pd.to_datetime(df['fecha'])
df['mes'] = df['fecha'].dt.to_period('M')

# INDICADORES CLAVE
ventas_totales = df['total_venta'].sum()
producto_mas_vendido = df.groupby('producto')['cantidad'].sum().idxmax()
ventas_por_mes = df.groupby('mes')['total_venta'].sum()

print(f'Ventas totales: ${ventas_totales:,.2f}')
print(f'Producto mas vendido: {producto_mas_vendido}')

# GRAFICO de evolucion mensual
fig, ax = plt.subplots(figsize=(10, 5))
ventas_por_mes.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
ax.set_title('Evolucion de Ventas por Mes - 2024', fontsize=14)
ax.set_xlabel('Mes')
ax.set_ylabel('Total Vendido ($)')
ax.tick_params(axis='x', rotation=45)
plt.tight_layout()
plt.savefig('resultados/grafico_ventas.png', dpi=150)
plt.close()
print('Grafico guardado en resultados/grafico_ventas.png')
